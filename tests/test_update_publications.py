"""Regression checks for publication presentation and citation generation.

Run with: python3 -B -m unittest discover -s tests -v
"""

from html.parser import HTMLParser
from pathlib import Path
import unittest

from update_publications import (
    bibtex_from_entry,
    clean_braces,
    format_entry,
    generate_featured_publication,
    generate_publications_md,
    parse_bibtex,
    publication_type_label,
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
            (ROOT / "Personal Publications.bib").read_text(encoding="utf-8")
        )

    def test_labels_use_publication_metadata_without_guessing(self):
        cases = [
            ({"type": "misc", "publisher": "arXiv"}, "Preprint"),
            ({"type": "misc", "doi": "10.48550/arXiv.1234"}, "Preprint"),
            ({"type": "misc", "url": "https://arxiv.org/abs/1234"}, "Preprint"),
            ({"type": "article", "journal": "arXiv"}, "Preprint"),
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
        self.assertEqual(labels["leins_ur5e_2025"], "")
        for entry in self.entries:
            if entry.get("publisher") == "arXiv":
                self.assertEqual(labels[entry["cite_key"]], "Preprint")

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
        years = {entry.get("year", "Unknown") for entry in self.entries}
        self.assertEqual(len(markup.with_class("publication-year")), len(years))
        self.assertEqual(len(markup.with_class("publication-card")), len(self.entries))
        self.assertLess(source.index(">2026</h2>"), source.index(">2025</h2>"))
        self.assertLess(source.index(">2025</h2>"), source.index(">2024</h2>"))
        self.assertLess(source.index("When Does LLM Orchestration"), source.index("LLM-Based Educational"))
        self.assertNotIn('href="#', source)
        self.assertIn('src="{{ "/assets/publications.js" | relative_url }}"', source)
        self.assertIn("example&amp;hl=en", source)

    def test_featured_publication_stays_outside_compact_list(self):
        source = generate_featured_publication(self.entries)
        self.assertNotIn("publications-page", source)
        self.assertNotIn("publication-type", source)
        self.assertNotIn("publication-cite", source)
        self.assertIn("Featured publication", source)


if __name__ == "__main__":
    unittest.main()
