---
name: update-publications
description: Refresh this Jekyll website from the Zotero BibLaTeX export Personal Publications biblatex.bib. Use when adding, updating, removing, or featuring publications; validate venue/date fields, preserve images and citation keys, regenerate pages, and run regression checks.
compatibility: Python 3 for generation and tests; Ruby and Bundler only for a full Jekyll build.
---

# Update publications

Use the existing generator. Do not create another parser, manually patch generated files, or hardcode paper-specific venue names.

## Scope and paths

Work from the repository root, where `update_publications.py` lives. The root is `../../..` relative to this skill directory.

- **Active source:** `Personal Publications biblatex.bib`, exported from Zotero using **BibLaTeX**.
- **Legacy reference only:** `Personal Publications.bib`. Do not merge it into the active export, silently fall back to it, or require the user to maintain both files.
- Generator and `PUBLICATIONS_SOURCE`: `update_publications.py`.
- Thumbnails: `IMAGE_MAPPINGS` in the generator and `assets/images/`.
- Homepage selection: `FEATURED_PUBLICATION_KEY` in the generator.
- Generated outputs: `publications.md` and `_includes/featured_publication.html`.
- Regression suite: `tests/test_update_publications.py`.

Read `AGENTS.md` and inspect `git status --short` before editing. Preserve unrelated work and the user's export. Ask before making presentation choices, replacing images, changing the homepage feature, or changing publication facts that were not supplied or verified. Refreshing supplied metadata does not require a redesign decision.

## 1. Inspect the export

1. Read the active export's diff and affected entries. Match entries by cite key, not file position; a moved entry is not necessarily a new paper.
2. Check unique cite keys, titles, authors, a publication `date` (or legacy `year`), and a URL or DOI.
3. Compare keys against `IMAGE_MAPPINGS` and `FEATURED_PUBLICATION_KEY`. A change of export format must not break thumbnails or the selected homepage paper.
4. Preserve official field values, protective capitalization braces, and citation types. The parser supports BibTeX and BibLaTeX; do not normalize the source into a reduced citation format.
5. Keep both export files excluded from Jekyll publishing. They may contain local attachment paths.

## 2. Resolve venue fields, not paper-specific overrides

Both the list and featured card use `display_venue()`:

1. Journal: `journal` or BibLaTeX `journaltitle`.
2. Proceedings Title: `booktitle` or `proceedingsTitle` aliases.
3. Conference Name: `conferenceName` / `conference_name`, `conference`, or BibLaTeX `eventtitle`.

Skip empty and whitespace-only fields. Proceedings Title wins when supplied; Conference Name is its fallback. The display helper normalizes case, spaces, underscores, and hyphens in field names. The featured card retains a final `publisher` fallback.

Zotero's BibLaTeX exporter writes its **Conference Name** as `eventtitle`, whereas the standard BibTeX export may omit it. Inspect the actual exported field rather than assuming a reference-manager UI field was included.

- Keep paper-type badges separate from venue names. `@inproceedings` identifies a conference paper, not a particular conference. `@software` explicitly identifies software; do not infer that type merely from a GitHub link.
- Do not guess a venue from an OpenReview URL, copy a name from another paper, or add a hardcoded per-paper mapping.
- If both proceedings and conference fields are absent, report the missing metadata and request an export containing it. Research an uncertain venue only when requested, using authoritative records and distinguishing submissions/workshops from main-conference papers.
- Venue resolution must not mutate the source entry or inject a synthesized `booktitle` into the copied citation.

## 3. Preserve publication-date precision

`publication_date_parts()`, `publication_year()`, and `format_publication_date()` share the same date handling for grouping, sorting, list cards, and the homepage feature.

- Prefer BibLaTeX `date`: `YYYY`, `YYYY-MM`, or `YYYY-MM-DD`.
- Otherwise use explicit legacy `year`/`month` fields.
- Retain the supplied precision. A year-only publication date displays only its year, even if `urldate` has a month/day.
- Never use `urldate` or `eventdate` as a substitute publication date. Do not fill missing components from the old export.
- Sort newest first by supplied year/month/day, then title; entries without a known month sort after dated entries in the same year.
- Flag missing or invalid dates instead of inventing them. Group undated entries under `Unknown`; do not treat that as valid evidence that migration succeeded.

## 4. Preserve images and homepage selection

- Verify mapped image files exist and reuse mappings for updated entries.
- For new entries without an image, ask for an asset or preference. Optimize supplied thumbnails as WebP, around 200–250px square and under 300KB, preserving meaningful figure content.
- If a cite key changes, update its image mapping and any matching featured key. Ask if the paper's identity is ambiguous.
- Do not automatically feature the newest paper. Keep the existing selection unless requested otherwise.
- Resolve a removed featured key before generation. Do not delete assets merely because an entry disappeared.

## 5. Generate and validate

From the repository root:

```bash
python3 -B update_publications.py
python3 -B -m unittest discover -s tests -v
git diff --check
```

Use `python` instead only if it is the available Python 3 executable. Generation and tests use the standard library; no Python packages are needed. Regenerate after changing the active export, generator, image mappings, or featured selection. Never edit either generated output manually.

Check:

- Exactly one card per parsed entry, with no duplicate keys or unintended removals.
- Actual Conference Name fallback and journal names appear from the active export, with correct type labels and dates; no unexpected `Unknown` year groups.
- Existing thumbnails and the selected homepage paper remain intact.
- Replaced preprint metadata does not leave stale venue, link, or citation information.
- Copied citations retain native BibLaTeX `date`, `journaltitle`, and `eventtitle` fields where supplied, rather than synthesized `year`, `month`, or `booktitle` fields. Source exports remain unchanged.
- Repeating generation leaves the generated files unchanged.
- The final diff contains only intended export, generator/asset, test, documentation, and generated changes.

A changed abstract alone may not alter visible cards; abstracts are not displayed. New source dates can legitimately reorder cards or remove previously inferred access-date months.

If Ruby/Bundler and project dependencies are already available, run `bundle exec jekyll build`. Inspect changed pages in a browser when available. Otherwise report the limitation and ask before installing tools or modifying dependency files. Do not treat old `_site/` files as proof of a fresh build or edit them manually.

## 6. Report and stop

Summarize the active source, changed publication metadata, checks performed, and missing fields or verification limits. Distinguish source updates from a deployed live site.

Do not commit, push, or deploy unless requested. Do not broaden a publication refresh into a redesign or change unrelated personal data.
