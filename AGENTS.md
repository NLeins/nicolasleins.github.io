# AGENTS.md

## Overview
This is a Jekyll-based personal publication/research website for sharing academic publications and research projects. The site uses Python scripts to generate publication pages from a Zotero BibLaTeX export.

## Build/Lint/Test Commands

### Jekyll Site
- `bundle install` – Install Ruby dependencies (Gemfile.lock present)
- `bundle exec jekyll serve` – Run local development server at http://localhost:4000
- `bundle exec jekyll build` – Build site to `_site/` directory
- `bundle exec jekyll clean` – Clean generated site

### Python Script
- `python3 update_publications.py` – Parse `Personal Publications biblatex.bib` and regenerate `publications.md` plus `_includes/featured_publication.html`
- `python3 -B -m unittest discover -s tests -v` – Run the standard-library publication regression suite

### Linting and Formatting
- **No linting configuration** found in the repository.
- For Python, follow PEP 8 (use `black`, `flake8`, or `pylint` if added).
- For Ruby, consider adding `.rubocop.yml` for style enforcement.
- For Markdown, use consistent heading levels and line breaks.

### Testing
- Publication regression tests live in `tests/test_update_publications.py` and use Python's standard-library `unittest`.
- Extend that suite when changing parsing, generated markup, venue labels, or citations.
- For Jekyll, consider using `htmlproofer` (via `bundle exec jekyll build` and `htmlproofer ./_site`) to check links and HTML validity.

## Code Style Guidelines

### Python (`update_publications.py`)
- **Imports**: Standard library first, then third-party, then local modules.
- **Naming**: `snake_case` for functions, variables, modules; `UPPER_CASE` for constants (e.g., `IMAGE_MAPPINGS`, `MONTH_MAP`).
- **Docstrings**: Use triple-quoted strings with description, parameters, and returns.
- **Error handling**: Use `try-except` with specific exception types; provide helpful error messages.
- **File paths**: Prefer `pathlib.Path` over `os.path` for cross-platform compatibility.
- **String formatting**: Use f-strings for readability (e.g., `f"Found {len(entries)} entries"`).
- **Regular expressions**: Use raw strings (`r'pattern'`); compile repeated patterns with `re.compile`.
- **Type hints**: Not currently used; consider adding for clarity.

### Ruby / Jekyll
- **Gemfile**: Follow standard Ruby gem syntax; pin versions only when necessary.
- **Jekyll config** (`_config.yml`): Keep YAML clean, use comments for sections.
- **Liquid templates** (`_includes/`, `_layouts/`):
  - Indent consistently (two spaces).
  - Use `{% raw %}{%-{% endraw %}` and `{% raw %}-%}{% endraw %}` to trim whitespace where appropriate.
  - Include ARIA roles and semantic HTML in markup.
- **SCSS** (`assets/main.scss`): Extend the Minima theme; add custom styles after `@import "minima";`.

### Markdown Content
- **Front matter**: Required for Jekyll pages (layout, title, permalink).
- **Headings**: Use ATX style (`#`, `##`, …) and match the theme’s hierarchy.
- **Links**: Use relative URLs for internal links (e.g., `[Bio](/bio/)`).
- **Images**: Optimize with WebP format; specify meaningful alt text.
- **Code blocks**: Use triple backticks with language identifier.

### BibLaTeX (`Personal Publications biblatex.bib`)

Export the Zotero collection as **BibLaTeX** into this active source file. `Personal Publications.bib` is a legacy reference, not another active input; do not merge the two exports.
- **Cite keys**: Format as `lastname_shorttitle_year` (e.g., `leins_investigating_2026`).
- **Authors**: Use “Last, First and Last, First” format.
- **Required fields**: `title`, `author`, publication `date` (or legacy `year`), `url` (or `doi`).
- **Venue fields**: Prefer `journal`/`journaltitle`, then Proceedings Title (`booktitle` / `proceedingsTitle`), then Conference Name (`conferenceName` / `conference_name`, `conference`, or `eventtitle`). Skip empty fields and preserve the official citation; do not hardcode per-paper venue names.
- **Dates**: Preserve `date` precision (`YYYY`, `YYYY-MM`, or `YYYY-MM-DD`); otherwise use legacy `year`/`month`. Never use access/event dates to fill publication dates or synthesize citation fields.
- **Optional fields**: `abstract`, `file`, and other official export fields.
- **Protective braces**: Use `{…}` only for preserving capitalization; the script strips them.

### File Organization
- **Jekyll standard**:
  - `_includes/` – reusable HTML snippets
  - `_layouts/` – page templates
  - `_posts/` – blog posts (format `YYYY-MM-DD-title.md`)
  - `_data/` – YAML data files (`person.yml`)
- **Assets**:
  - `assets/images/` – publication thumbnails and site images
  - `assets/main.scss` – custom styles
- **Generated files**:
  - `publications.md` – auto-generated; **do not edit manually**.
  - `_site/` – built site; ignored by Git.

## Publication Update Skill

For publication refreshes, read `.agents/skills/update-publications/SKILL.md` and follow its metadata, image, generation, and validation workflow. In Pi, reload resources with `/reload` and invoke `/skill:update-publications` explicitly if needed.

A conference entry's `@inproceedings` type supplies a paper-type label, not a conference name. `display_venue()` falls back from an empty Proceedings Title to Conference Name using actual exported fields, without changing copied citations. In Zotero BibLaTeX, Conference Name is `eventtitle`, journal names use `journaltitle`, and publication dates use `date`. If the reference-manager UI has a field missing from the export, request an export containing that metadata. Never infer a venue from an OpenReview URL or add a hardcoded per-paper mapping.

## Publication Workflow (Condensed)

### Adding a New Publication
1. Update Zotero and export the collection as BibLaTeX to `Personal Publications biblatex.bib`, retaining stable cite keys.
2. Place an optimized image (WebP, ≤300 KB) in `assets/images/`.
3. Add its cite-key mapping to `IMAGE_MAPPINGS` in `update_publications.py`.
4. Run `python3 update_publications.py` and the regression suite.
5. Review both generated outputs and commit only when requested.

### Updating an Existing Publication
1. Re-export the updated collection to `Personal Publications biblatex.bib`.
2. Run `python3 update_publications.py` and the regression suite.
3. Review metadata, images, and copied citations; commit only when requested.

### Removing a Publication
1. Remove the item from the Zotero collection and re-export the active BibLaTeX file.
2. Resolve a removed featured key; do not delete assets without authorization.
3. Run `python3 update_publications.py` and the regression suite.
4. Review the diff and commit only when requested.

## Agent Instructions
- **Always run** `python3 update_publications.py` after modifying `Personal Publications biblatex.bib`, the generator (including date/venue resolution), `IMAGE_MAPPINGS`, or `FEATURED_PUBLICATION_KEY`.
- The script is idempotent; safe to run multiple times.
- Publications are grouped by year (newest first).
- Check `IMAGE_MAPPINGS` before adding new BibTeX entries—mapping is required for images to display.
- Use consistent cite-key naming: `lastname_shortitle_year`.
- Never edit `publications.md` manually; it is generated by the script.
- When adding images, optimize them (WebP, 200–250 px square, <300 KB) to maintain site performance.

## Cursor / Copilot Rules
- No `.cursor/rules/` or `.cursorrules` files present.
- No `.github/copilot-instructions.md` file present.
- Consider adding repository-specific rules if using Cursor or GitHub Copilot.

---

*This file is intended for agentic coding assistants working in this repository. Keep it updated as the project evolves.*