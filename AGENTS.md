# Repository Documentation

## Overview
This is a Jekyll-based personal publication/research website for sharing academic publications and research projects.

## Key Files & Structure

### Main Content Files
- **Personal Publications.bib** - BibTeX bibliography file containing all publications and projects
- **update_publications.py** - Python script that parses the .bib file and generates publications.md
- **publications.md** - Auto-generated publications page (output of update_publications.py)
- **_config.yml** - Jekyll configuration
- **index.md, blog.md, bio.md** - Main site pages
- **assets/images/** - Directory containing publication thumbnail images

### Data & Includes
- **_data/person.yml** - Personal information data
- **_includes/** - Jekyll template includes
- **_posts/** - Blog posts directory

## Workflow: Adding New Publications

### Step 1: Add to Bibliography
1. Add new entry to `Personal Publications.bib` in BibTeX format
2. Use consistent cite key format: `lastname_shortitle_year` (e.g., `leins_investigating_2026`)

### Step 2: Add Image
1. Add corresponding publication image to `assets/images/`
2. Supported formats: `.png`, `.jpg`
3. Recommended size: Square aspect ratio works best (180x180px display)

### Step 3: Update Image Mappings
1. Open `update_publications.py`
2. Add entry to `IMAGE_MAPPINGS` dictionary (lines 12-17):
   ```python
   'cite_key': 'image_filename',
   ```
3. Example:
   ```python
   'gonnermann-muller_facet_2026': 'facet.png',
   ```

### Step 4: Generate Publications Page
Run: `python update_publications.py`

This generates:
- Parses all BibTeX entries
- Groups publications by year (descending order)
- Creates HTML cards with images, titles, authors, venues, and links
- Outputs to `publications.md`

## Current Publications

### 2024
- **gonnermann-muller_value_2024** - "Value by Design: Reducing Cognitive Load..." (ICIS 2024)
  - Image: `fig_ICIS.png`
- **leins_comparing_2024** - "Comparing head-mounted and handheld augmented reality..." (Journal on Multimodal User Interfaces)
  - Image: `fig_springerVR.jpg`

### 2025
- **leins_ur5e_2025** - "UR5e Augmented Reality Interface on Meta Quest 3"
  - Image: `fig_RobotAR.png`

### 2026
- **haase_within-model_2026** - "Within-Model vs Between-Prompt Variability in Large Language Models..." (arXiv)
  - Image: `Within_Between.png`
- **gonnermann-muller_facet_2026** - "FACET: Multi-Agent AI Supporting Teachers..." (arXiv)
  - Image: `facet.png`
- **leins_investigating_2026** - "Investigating the Influence of Spatial Ability in Augmented Reality-assisted Robot Programming" (arXiv)
  - Image: `SA-in-robiotics.png`

## Image Mappings (IMAGE_MAPPINGS Dictionary)

All publication cite keys must have a corresponding entry mapping to an image file. Current mappings in `update_publications.py`:

```python
IMAGE_MAPPINGS = {
    'gonnermann-muller_value_2024': 'fig_ICIS.png',
    'leins_comparing_2024': 'fig_springerVR.jpg',
    'leins_ur5e_2025': 'fig_RobotAR.png',
    'haase_within-model_2026': 'Within_Between.png',
    'gonnermann-muller_facet_2026': 'facet.png',
    'leins_investigating_2026': 'SA-in-robiotics.png',
}
```

## Publication Card Format

Each publication is displayed as an HTML card with:
- **Image**: 180x180px thumbnail (if mapped in IMAGE_MAPPINGS)
- **Title**: From BibTeX `title` field
- **Authors**: From BibTeX `author` field (formatted as "First Last" names)
- **Venue & Year**: From `journal`/`booktitle` and `year` fields
- **Links**: Generated from `url` and `doi` fields
  - GitHub URLs → "Code" link
  - arXiv URLs → "arXiv" link
  - DOI → "DOI" link
  - Other URLs → "Link"

## BibTeX Entry Fields

Required/common fields in entries:
- `title` - Publication title
- `author` - Author list (format: "Last, First and Last, First")
- `year` - Publication year
- `month` - Publication month (optional)
- `journal` - Journal name (for articles)
- `booktitle` - Conference/proceedings title (for conference papers)
- `url` - Link to publication or resource
- `doi` - DOI identifier (optional)
- `abstract` - Publication abstract (stored but not displayed)
- `file` - Zotero file references (metadata, not displayed)

## Script Details (update_publications.py)

### Key Functions
- **parse_bibtex()** - Parses BibTeX file and extracts entries
- **format_entry()** - Formats a single entry as HTML card
- **format_authors()** - Converts author names from "Last, First" to "First Last"
- **clean_braces()** - Removes protective braces from BibTeX text
- **generate_publications_md()** - Groups entries by year and generates full MD file

### Processing
- Entries grouped by year in descending order
- Protective braces `{Text}` removed from titles and venues
- HTML cards use CSS Grid for image + content layout
- Images display only if mapped in IMAGE_MAPPINGS
- Output file: `publications.md`

## Common Tasks

### Add a new publication
1. Add BibTeX entry to `Personal Publications.bib`
2. Save image to `assets/images/`
3. Add mapping to `IMAGE_MAPPINGS` in `update_publications.py`
4. Run `python update_publications.py`
5. Commit changes

### Update existing publication
1. Edit entry in `Personal Publications.bib`
2. Run `python update_publications.py`
3. Commit changes

### Update publication image
1. Replace image file in `assets/images/`
2. No script changes needed (mapping stays the same)
3. Run `python update_publications.py` to regenerate
4. Commit changes

### Remove a publication
1. Delete entry from `Personal Publications.bib`
2. Optionally remove image from `assets/images/` if unused
3. Optionally remove mapping from `IMAGE_MAPPINGS`
4. Run `python update_publications.py`
5. Commit changes

## Assets & Images

Directory: `assets/images/`

Current images:
- `fig_ICIS.webp` - 2024 ICIS publication
- `fig_springerVR.webp` - Springer VR journal article
- `fig_RobotAR.webp` - Robot AR interface
- `Within_Between.webp` - LLM variability study
- `facet.webp` - FACET education AI system
- `SA-in-robotics.webp` - Spatial ability in AR robotics
- `profile.jpg` - Profile picture

## Image Optimization

**IMPORTANT:** Images must be optimized before adding to the repo to avoid performance issues.

### Requirements
- **Display size:** 180x180px
- **File size target:** 100-300 KB per image
- **Recommended dimensions:** 200-250px (accounts for retina displays and scales down smoothly)
- **Aspect ratio:** Square (1:1 ratio works best)

### Format Recommendations
- **WebP:** Preferred format for this repo. Modern, smaller files, widely supported in browsers. Tools: cwebp (CLI) or online converters
- **PNG:** Use for images with sharp edges or text. Compress with TinyPNG or ImageOptim
- **JPG:** Use for photographs. Quality 75-85% works well

### Optimization Process
1. **Resize** to 200-250px max dimension (square)
2. **Compress** using:
   - TinyPNG/TinyJPG (online, very effective)
   - ImageOptim (macOS)
   - ImageMagick command line: `convert image.png -resize 250x250 -quality 85 output.jpg`
3. **Target:** Final file size should be **< 300 KB** (ideally 100-200 KB)

### Performance Impact
- Unoptimized large images (1-3+ MB) cause:
  - Slower page loads
  - Increased bandwidth usage
  - Browser rendering strain, especially during animations
  - Potential flickering during hover effects

### Verification
After adding images, check file sizes:
```bash
ls -lh assets/images/
```
Each publication image should be well under 500 KB.

## Technology Stack
- **Jekyll** - Static site generator
- **Ruby** - Jekyll framework
- **Python 3** - Publication processing script
- **BibTeX** - Bibliography format
- **Markdown** - Content format

## Notes for Claude Agents
- This is a Jekyll site with Python-driven publication management
- Always run `update_publications.py` after modifying `Personal Publications.bib` or `IMAGE_MAPPINGS`
- The script is idempotent—safe to run multiple times
- All publications are grouped by year (newest first)
- Check `IMAGE_MAPPINGS` before adding new BibTeX entries—mapping is required for images to display
- Use consistent cite key naming: `lastname_shortitle_year`
