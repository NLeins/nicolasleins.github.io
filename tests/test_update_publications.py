"""Regression checks for publication presentation and citation generation.

Run with: python3 -B -m unittest discover -s tests -v
"""

from html.parser import HTMLParser
from pathlib import Path
import unittest
from unittest.mock import patch

from update_publications import (
    IMAGE_MAPPINGS,
    PUBLICATIONS_SOURCE,
    bibtex_from_entry,
    clean_braces,
    display_venue,
    format_entry,
    format_publication_date,
    generate_featured_publication,
    generate_publications_md,
    parse_bibtex,
    publication_date_parts,
    publication_type_label,
    publication_year,
)


ROOT = Path(__file__).resolve().parents[1]


class Markup(HTMLParser):
    """Collect element attributes and verify matching generated block tags."""

    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.elements = []
        self.stack = []
        self.feed(source)
        if self.stack:
            raise AssertionError(f"Unclosed tags: {self.stack}")

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))
        if tag not in {"img", "br", "hr", "input", "link", "meta"}:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack.pop() != tag:
            raise AssertionError(f"Unmatched closing tag: {tag}")

    def with_class(self, name):
        return [
            (tag, attrs)
            for tag, attrs in self.elements
            if name in attrs.get("class", "").split()
        ]


class PublicationPresentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = parse_bibtex(
            (ROOT / PUBLICATIONS_SOURCE).read_text(encoding="utf-8")
        )

    def test_labels_use_publication_metadata_without_guessing(self):
        cases = [
            ({"type": "misc", "publisher": "arXiv"}, "Preprint"),
            ({"type": "misc", "doi": "10.48550/arXiv.1234"}, "Preprint"),
            ({"type": "misc", "url": "https://arxiv.org/abs/1234"}, "Preprint"),
            ({"type": "article", "journal": "arXiv"}, "Preprint"),
            ({"type": "article", "journaltitle": "arXiv"}, "Preprint"),
            ({"type": "article", "journaltitle": "ICIS 2024 Proceedings"},
             "Conference paper"),
            ({"type": "article", "journaltitle": "A Journal"},
             "Journal article"),
            ({"type": "software"}, "Software"),
            ({"type": "inproceedings"}, "Conference paper"),
            ({"type": "article", "journal": "ICIS 2024 Proceedings"}, "Conference paper"),
            ({"type": "article", "journal": "Journal on Multimodal User Interfaces"}, "Journal article"),
            # A published article remains an article even with an arXiv URL.
            ({"type": "article", "journal": "A Journal", "url": "https://arxiv.org/abs/1234"}, "Journal article"),
            ({"type": "misc", "url": "https://github.com/example/project"}, ""),
            # Mentioning arXiv in an unrelated URL is not preprint evidence.
            ({"type": "misc", "url": "https://example.org/?q=arxiv"}, ""),
            ({"type": "misc", "url": "https://arxiv.org.example.org/"}, ""),
            ({}, ""),
        ]
        for entry, expected in cases:
            with self.subTest(entry=entry):
                self.assertEqual(publication_type_label(entry), expected)

    def test_real_entries_have_expected_labels(self):
        labels = {entry["cite_key"]: publication_type_label(entry) for entry in self.entries}
        self.assertEqual(labels["gonnermann-muller_value_2024"], "Conference paper")
        self.assertEqual(labels["leins_comparing_2024"], "Journal article")
        self.assertEqual(labels["leins_beyond_2026"], "Conference paper")
        self.assertEqual(labels["leins_ur5e_2025"], "Software")
        for entry in self.entries:
            if clean_braces(entry.get("publisher", "")).lower() == "arxiv":
                self.assertEqual(labels[entry["cite_key"]], "Preprint")

    def test_display_venue_supports_official_fields_and_precedence(self):
        cases = [
            ({"cite_key": "haase_within-model_2026"}, ""),
            ({"booktitle": "Proceedings", "conferenceName": "NeurIPS"},
             "Proceedings"),
            ({"journal": "A Journal", "booktitle": "Proceedings"},
             "A Journal"),
            ({"journaltitle": "{BibLaTeX} Journal", "booktitle": "Proceedings"},
             "BibLaTeX Journal"),
            ({"journal": " ", "booktitle": "Proceedings"}, "Proceedings"),
            ({"proceedingsTitle": "Proceedings", "conferenceName": "NeurIPS"},
             "Proceedings"),
            ({"booktitle": "", "conferenceName": "NeurIPS"}, "NeurIPS"),
            ({"proceedings_title": " ", "conference_name": "NeurIPS"},
             "NeurIPS"),
            ({"Proceedings Title": "", "Conference Name": "NeurIPS"},
             "NeurIPS"),
            ({"booktitle": "{ }", "eventtitle": "{NeurIPS} Workshop"},
             "NeurIPS Workshop"),
            ({"conference": "Example Conference"}, "Example Conference"),
            ({"type": "misc", "publisher": "arXiv"}, ""),
            ({"url": "https://openreview.net/forum?id=other"}, ""),
            ({}, ""),
        ]
        for entry, expected in cases:
            with self.subTest(entry=entry):
                self.assertEqual(display_venue(entry), expected)

    def test_conference_name_fallback_preserves_exported_bibtex(self):
        entry = parse_bibtex('''@inproceedings{example,
            title = {Test paper},
            booktitle = {},
            conferenceName = {NeurIPS},
            month = sep,
            year = {2026},
        }''')[0]
        original = dict(entry)
        citation = bibtex_from_entry(entry)
        source = format_entry(entry)
        self.assertIn("NeurIPS, Sep 2026", source)
        copied = Markup(source).with_class("publication-cite")[0][1]
        self.assertEqual(copied["data-bibtex"], citation)
        self.assertIn("conferencename = {NeurIPS}", citation)
        self.assertNotIn("booktitle = {NeurIPS}", citation)
        self.assertEqual(entry, original)

    def test_featured_card_uses_same_conference_name_fallback(self):
        entry = {
            "cite_key": "example", "title": "Test paper", "booktitle": "",
            "conference_name": "NeurIPS", "month": "sep", "year": "2026",
        }
        with patch("update_publications.FEATURED_PUBLICATION_KEY", "example"):
            source = generate_featured_publication([entry])
        self.assertIn("NeurIPS, Sep 2026", source)

    def test_conference_name_fallback_is_escaped(self):
        source = format_entry({"title": "Test", "conferenceName": "A <B> & C"})
        self.assertIn("A &lt;B&gt; &amp; C", source)
        self.assertNotIn("A <B>", source)

    def test_each_citation_button_preserves_exact_bibtex(self):
        for entry in self.entries:
            with self.subTest(key=entry["cite_key"]):
                markup = Markup(format_entry(entry))
                buttons = markup.with_class("publication-cite")
                self.assertEqual(len(buttons), 1)
                tag, attrs = buttons[0]
                self.assertEqual(tag, "button")
                self.assertEqual(attrs["type"], "button")
                self.assertEqual(attrs["data-bibtex"], bibtex_from_entry(entry))
                self.assertIn(clean_braces(entry["title"]), attrs["aria-label"])
                status = markup.with_class("publication-copy-status")[0][1]
                self.assertEqual(status["role"], "status")
                self.assertEqual(status["aria-live"], "polite")
                self.assertNotIn(" | ", format_entry(entry))

    def test_image_panels_preserve_figures_and_have_descriptive_alt(self):
        for entry in self.entries:
            markup = Markup(format_entry(entry))
            images = [attrs for tag, attrs in markup.elements if tag == "img"]
            self.assertEqual(len(images), 1)
            self.assertEqual(images[0]["loading"], "lazy")
            self.assertIn(clean_braces(entry["title"]), images[0]["alt"])

    def test_entries_without_images_have_balanced_markup(self):
        markup = Markup(format_entry({"cite_key": "unmapped", "title": "No image"}))
        self.assertEqual(len(markup.with_class("publication-content")), 1)
        self.assertEqual(markup.with_class("publication-grid"), [])
        self.assertEqual(markup.with_class("publication-type"), [])

    def test_text_and_attribute_values_are_escaped(self):
        entry = {
            "title": 'A <script> & "quoted" title',
            "author": "Example, A < B",
            "journal": "Research & <Studies>",
            "url": 'https://example.org/?a=1&b="two"',
        }
        source = format_entry(entry)
        self.assertNotIn("<script>", source)
        self.assertIn("&lt;script&gt;", source)
        self.assertIn("Research &amp; &lt;Studies&gt;", source)
        markup = Markup(source)
        links = [attrs for tag, attrs in markup.elements if tag == "a"]
        self.assertEqual(links[0]["href"], entry["url"])

    def test_years_and_entries_remain_newest_first_without_jump_links(self):
        source = generate_publications_md(self.entries, "example&hl=en")
        markup = Markup(source.split("---", 2)[2])
        years = {publication_year(entry) for entry in self.entries}
        self.assertEqual(len(markup.with_class("publication-year")), len(years))
        self.assertEqual(len(markup.with_class("publication-card")), len(self.entries))
        self.assertLess(source.index(">2026</h2>"), source.index(">2025</h2>"))
        self.assertLess(source.index(">2025</h2>"), source.index(">2024</h2>"))
        self.assertLess(source.index("When Does LLM Orchestration"), source.index("LLM-Based Educational"))
        self.assertNotIn('href="#', source)
        self.assertIn('src="{{ "/assets/publications.js" | relative_url }}"', source)
        self.assertIn("example&amp;hl=en", source)

    def test_biblatex_dates_preserve_precision_and_ignore_access_dates(self):
        cases = [
            ({"date": "2026-09-24"}, (2026, 9, 24), "Sep 2026"),
            ({"date": "2026-08"}, (2026, 8, 0), "Aug 2026"),
            ({"date": "2026", "urldate": "2026-10-20"},
             (2026, 0, 0), "2026"),
            ({"date": "2026-08", "year": "2025", "month": "jan"},
             (2026, 8, 0), "Aug 2026"),
            ({"date": "2026", "month": "sep"}, (2026, 0, 0), "2026"),
            ({"year": "2025", "month": "sep"}, (2025, 9, 0), "Sep 2025"),
            ({"year": "2025", "urldate": "2026-08-25"},
             (2025, 0, 0), "2025"),
            ({"urldate": "2026-09-24"}, (0, 0, 0), ""),
            ({"eventdate": "2026-09-24"}, (0, 0, 0), ""),
            ({"date": "2026-02-30"}, (0, 0, 0), ""),
            ({"date": "2026-00-01"}, (0, 0, 0), ""),
            ({"date": "2024-02-29"}, (2024, 2, 29), "Feb 2024"),
            ({}, (0, 0, 0), ""),
        ]
        for entry, expected_parts, expected_text in cases:
            with self.subTest(entry=entry):
                self.assertEqual(publication_date_parts(entry), expected_parts)
                self.assertEqual(format_publication_date(entry), expected_text)
                year = expected_parts[0]
                self.assertEqual(
                    publication_year(entry), str(year) if year else "Unknown"
                )

    def test_new_export_preserves_keys_images_and_actual_conference_name(self):
        legacy = parse_bibtex(
            (ROOT / "Personal Publications.bib").read_text(encoding="utf-8")
        )
        keys = [entry["cite_key"] for entry in self.entries]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual(set(keys), {entry["cite_key"] for entry in legacy})
        for entry in self.entries:
            self.assertGreater(publication_date_parts(entry)[0], 0)
            image = ROOT / "assets/images" / IMAGE_MAPPINGS[entry["cite_key"]]
            self.assertTrue(image.is_file())
        within = next(entry for entry in self.entries
                      if entry["cite_key"] == "haase_within-model_2026")
        self.assertFalse(within.get("booktitle"))
        self.assertEqual(display_venue(within), within["eventtitle"])
        source = generate_publications_md(self.entries)
        self.assertIn(within["eventtitle"], source)
        self.assertNotIn(">Unknown</h2>", source)

    def test_copied_biblatex_keeps_original_date_and_venue_fields(self):
        for entry in self.entries:
            original = dict(entry)
            copied = parse_bibtex(bibtex_from_entry(entry))[0]
            self.assertEqual(copied["date"], entry["date"])
            for field in ("journaltitle", "eventtitle", "booktitle"):
                if field in entry:
                    self.assertEqual(copied[field], entry[field])
            self.assertNotIn("year", copied)
            self.assertNotIn("month", copied)
            self.assertEqual(entry, original)

    def test_legacy_bibtex_still_renders_without_mutating_entries(self):
        entries = parse_bibtex(
            (ROOT / "Personal Publications.bib").read_text(encoding="utf-8")
        )
        originals = [dict(entry) for entry in entries]
        source = generate_publications_md(entries)
        self.assertIn(">2026</h2>", source)
        self.assertIn("Journal on Multimodal User Interfaces", source)
        self.assertEqual(entries, originals)
        markup = Markup(source.split("---", 2)[2])
        self.assertEqual(len(markup.with_class("publication-card")), len(entries))

    def test_date_sorting_uses_full_date_and_places_unknown_months_last(self):
        entries = [
            {"title": "Year only", "date": "2026"},
            {"title": "Earlier", "date": "2026-09-23"},
            {"title": "Latest", "date": "2026-09-24"},
            {"title": "Earlier year", "date": "2025-12-31"},
        ]
        source = generate_publications_md(entries)
        titles = ["Latest", "Earlier", "Year only", "Earlier year"]
        locations = [source.index(f'>{title}</h3>') for title in titles]
        self.assertEqual(locations, sorted(locations))

    def test_featured_biblatex_date_is_not_lost(self):
        entry = {"cite_key": "example", "title": "Test", "date": "2026-08-01"}
        with patch("update_publications.FEATURED_PUBLICATION_KEY", "example"):
            source = generate_featured_publication([entry])
        self.assertIn("Aug 2026", source)

    def test_featured_publication_stays_outside_compact_list(self):
        source = generate_featured_publication(self.entries)
        self.assertNotIn("publications-page", source)
        self.assertNotIn("publication-type", source)
        self.assertNotIn("publication-cite", source)
        self.assertIn("Featured publication", source)


if __name__ == "__main__":
    unittest.main()
