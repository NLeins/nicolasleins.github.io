# AGENTS.md

## Overview
This is a Jekyll-based personal publication/research website for sharing academic publications and research projects. The site uses Python scripts to generate publication pages from BibTeX entries.

## Build/Lint/Test Commands

### Jekyll Site
- `bundle install` – Install Ruby dependencies (Gemfile.lock present)
- `bundle exec jekyll serve` – Run local development server at http://localhost:4000
- `bundle exec jekyll build` – Build site to `_site/` directory
- `bundle exec jekyll clean` – Clean generated site

### Python Script
- `python update_publications.py` – Parse `Personal Publications.bib` and generate `publications.md`
- `python -m pytest` – No test suite currently defined; consider adding `test_update_publications.py`

### Linting and Formatting
- **No linting configuration** found in the repository.
- For Python, follow PEP 8 (use `black`, `flake8`, or `pylint` if added).
- For Ruby, consider adding `.rubocop.yml` for style enforcement.
- For Markdown, use consistent heading levels and line breaks.

### Testing
- No test suite currently exists.
- To add Python tests, create `test_update_publications.py` with unit tests for `parse_bibtex`, `format_entry`, etc.
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

### BibTeX (`Personal Publications.bib`)
- **Cite keys**: Format as `lastname_shorttitle_year` (e.g., `leins_investigating_2026`).
- **Authors**: Use “Last, First and Last, First” format.
- **Required fields**: `title`, `author`, `year`, `url` (or `doi`), `journal`/`booktitle`.
- **Optional fields**: `month`, `abstract`, `file`.
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

## Publication Workflow (Condensed)

### Adding a New Publication
1. Add BibTeX entry to `Personal Publications.bib` with required fields.
2. Place optimized image (WebP, ≤300 KB, square aspect ratio) in `assets/images/`.
3. Add mapping `'cite_key': 'image_filename.webp'` to `IMAGE_MAPPINGS` in `update_publications.py`.
4. Run `python update_publications.py`.
5. Commit changes (BibTeX, image, script, and generated `publications.md`).

### Updating an Existing Publication
1. Edit the entry in `Personal Publications.bib`.
2. Run `python update_publications.py`.
3. Commit changes.

### Removing a Publication
1. Delete entry from `Personal Publications.bib`.
2. Optionally remove image file and mapping.
3. Run `python update_publications.py`.
4. Commit changes.

## Agent Instructions
- **Always run** `python update_publications.py` after modifying `Personal Publications.bib` or `IMAGE_MAPPINGS`.
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