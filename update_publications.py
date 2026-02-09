#!/usr/bin/env python3
"""
Parse BibTeX file and generate publications.md for Jekyll site.
Usage: python update_publications.py
"""

import re
from collections import defaultdict
from pathlib import Path

# Image mappings: cite_key -> image filename
IMAGE_MAPPINGS = {
    'gonnermann-muller_value_2024': 'fig_ICIS.webp',
    'leins_comparing_2024': 'fig_springerVR.webp',
    'leins_ur5e_2025': 'fig_RobotAR.webp',
    'haase_within-model_2026': 'Within_Between.webp',
    'gonnermann-muller_facet_2026': 'facet.webp',
    'leins_investigating_2026': 'SA-in-robotics.webp',
    'gonnermann-muller_stable_2026': 'adhd.webp',
}

MONTH_MAP = {
    'jan': 1,
    'january': 1,
    'feb': 2,
    'february': 2,
    'mar': 3,
    'march': 3,
    'apr': 4,
    'april': 4,
    'may': 5,
    'jun': 6,
    'june': 6,
    'jul': 7,
    'july': 7,
    'aug': 8,
    'august': 8,
    'sep': 9,
    'sept': 9,
    'september': 9,
    'oct': 10,
    'october': 10,
    'nov': 11,
    'november': 11,
    'dec': 12,
    'december': 12,
}


def month_to_num(month):
    """Convert month string to number; unknown -> 0."""
    if not month:
        return 0
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', str(month)).lower()
    if cleaned.isdigit():
        return int(cleaned)
    if cleaned in MONTH_MAP:
        return MONTH_MAP[cleaned]
    if len(cleaned) >= 3 and cleaned[:3] in MONTH_MAP:
        return MONTH_MAP[cleaned[:3]]
    return 0


def year_to_int(year):
    """Convert year string to int; unknown -> 0."""
    try:
        return int(str(year).strip())
    except (TypeError, ValueError):
        return 0


def parse_bibtex(bib_content):
    """Parse BibTeX content and return list of entries."""
    entries = []

    # Find all entry starts
    entry_pattern = r'@(\w+)\s*\{\s*([^,]+)\s*,'
    entry_matches = list(re.finditer(entry_pattern, bib_content))

    for i, match in enumerate(entry_matches):
        entry_type = match.group(1).lower()
        cite_key = match.group(2).strip()

        # Find the content between this entry and the next (or end of file)
        start = match.end()
        if i + 1 < len(entry_matches):
            end = entry_matches[i + 1].start()
        else:
            end = len(bib_content)

        fields_str = bib_content[start:end]

        # Find the closing brace of this entry
        brace_count = 1
        entry_end = 0
        for j, char in enumerate(fields_str):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    entry_end = j
                    break

        fields_str = fields_str[:entry_end]

        entry = {
            'type': entry_type,
            'cite_key': cite_key
        }

        # Parse fields (both braced {value} and unquoted value formats)
        pos = 0
        while pos < len(fields_str):
            # Find field name and equals sign
            field_match = re.match(r'\s*(\w+)\s*=\s*', fields_str[pos:])
            if not field_match:
                # Try to find next field
                next_field = re.search(r'\s*(\w+)\s*=\s*', fields_str[pos + 1:])
                if next_field:
                    pos += next_field.start() + 1
                    continue
                else:
                    break

            field_name = field_match.group(1).lower()
            pos += field_match.end()

            # Check if value is in braces or unquoted
            if pos < len(fields_str) and fields_str[pos] == '{':
                # Braced value
                pos += 1  # Skip opening brace
                brace_count = 1
                value_start = pos
                value_end = pos
                while pos < len(fields_str) and brace_count > 0:
                    if fields_str[pos] == '{':
                        brace_count += 1
                    elif fields_str[pos] == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            value_end = pos
                            break
                    pos += 1
                field_value = fields_str[value_start:value_end].strip()
                pos += 1  # Skip closing brace
            else:
                # Unquoted value (read until comma or end)
                value_start = pos
                while pos < len(fields_str) and fields_str[pos] not in [',', '}']:
                    pos += 1
                field_value = fields_str[value_start:pos].strip()

            entry[field_name] = field_value

        entries.append(entry)

    return entries


def format_authors(authors_str):
    """Format author string for display."""
    # Split by 'and'
    authors = [a.strip() for a in authors_str.split(' and ')]

    # Format each author (Last, First -> First Last)
    formatted = []
    for author in authors:
        if ',' in author:
            parts = [p.strip() for p in author.split(',')]
            formatted.append(f"{parts[1]} {parts[0]}")
        else:
            formatted.append(author)

    return ', '.join(formatted)


def clean_braces(text):
    """Remove protective braces from BibTeX text."""
    # Remove single-word protective braces: {Word} -> Word
    text = re.sub(r'\{(\w+)\}', r'\1', text)
    # Remove protective braces around phrases: {Multiple Words} -> Multiple Words
    text = re.sub(r'\{([^{}]+)\}', r'\1', text)
    return text


def format_entry(entry):
    """Format a single BibTeX entry as HTML card."""
    cite_key = entry.get('cite_key', '')
    image_file = IMAGE_MAPPINGS.get(cite_key)

    html_parts = []

    # Start card container
    html_parts.append('<div class="card publication-card">')

    # If there's an image, create a two-column layout
    if image_file:
        html_parts.append('<div style="display: grid; grid-template-columns: 180px 1fr; gap: 24px; align-items: center;">')
        html_parts.append(f'  <div style="width: 180px; height: 180px; overflow: hidden; border-radius: 4px; flex-shrink: 0; will-change: transform; transform: translateZ(0); contain: layout style paint;">')
        html_parts.append(f'    <img src="/assets/images/{image_file}" alt="Publication" style="width: 100%; height: 100%; object-fit: cover;">')
        html_parts.append('  </div>')
        html_parts.append('  <div>')

    # Title
    title = entry.get('title', 'Untitled')
    title = clean_braces(title)
    html_parts.append(f"    <h3 style=\"margin-top: 0; font-size: 1.3em; margin-bottom: 12px;\">{title}</h3>")

    # Authors
    if 'author' in entry:
        authors = format_authors(entry['author'])
        html_parts.append(f"    <div style=\"color: #4b5563; margin-bottom: 12px; font-size: 1.05em;\">{authors}</div>")

    # Venue and year
    venue_parts = []
    if 'journal' in entry:
        journal = clean_braces(entry['journal'])
        venue_parts.append(journal)
    elif 'booktitle' in entry:
        booktitle = clean_braces(entry['booktitle'])
        venue_parts.append(booktitle)

    # Build date string
    date_parts = []
    if 'month' in entry:
        date_parts.append(entry['month'].capitalize())
    if 'year' in entry:
        date_parts.append(entry['year'])

    if date_parts:
        venue_parts.append(' '.join(date_parts))

    if venue_parts:
        html_parts.append(f"    <div style=\"color: #6b7280; font-size: 1em; margin-bottom: 14px;\">{', '.join(venue_parts)}</div>")

    # Links
    links = []
    if 'url' in entry:
        url = entry['url']
        if 'github.com' in url:
            links.append(f"<a href=\"{url}\">Code</a>")
        elif 'arxiv.org' in url:
            links.append(f"<a href=\"{url}\">arXiv</a>")
        else:
            links.append(f"<a href=\"{url}\">Link</a>")

    if 'doi' in entry:
        links.append(f"<a href=\"https://doi.org/{entry['doi']}\">DOI</a>")

    if links:
        html_parts.append(f"    <div style=\"font-size: 1.05em;\">{' | '.join(links)}</div>")

    # Close grid if image was present
    if image_file:
        html_parts.append('  </div>')
        html_parts.append('</div>')

    html_parts.append('</div>')

    return '\n'.join(html_parts)


def generate_publications_md(entries, scholar_id=None):
    """Generate the full publications.md content with HTML cards."""
    # Group entries by year
    by_year = defaultdict(list)
    for entry in entries:
        year = entry.get('year', 'Unknown')
        by_year[year].append(entry)

    # Sort years descending (numeric if possible)
    sorted_years = sorted(by_year.keys(), key=year_to_int, reverse=True)

    # Build HTML content
    md_lines = [
        "---",
        "layout: page",
        "title: Publications",
        "permalink: /publications/",
        "---",
        "<style>.post-header { display: none; }</style>",
        "",
        "<h1 style=\"font-size: 2.5em; margin-bottom: 20px;\">Publications</h1>",
    ]

    if scholar_id:
        md_lines.append(f'<p style="font-size: 1.1em; margin-bottom: 30px;">For a complete list, see my <a href="https://scholar.google.com/citations?user={scholar_id}">Google Scholar profile</a>.</p>')

    md_lines.append("")

    # Add entries by year
    for year in sorted_years:
        md_lines.append(f'<div style="margin-bottom: 40px;">')
        md_lines.append(f"  <h2 style=\"margin-bottom: 28px; font-size: 1.8em;\">{year}</h2>")

        by_year[year].sort(
            key=lambda e: (
                year_to_int(e.get('year')),
                month_to_num(e.get('month')),
                clean_braces(e.get('title', '')).lower(),
            ),
            reverse=True,
        )

        for entry in by_year[year]:
            md_lines.append("  " + format_entry(entry).replace('\n', '\n  '))

        md_lines.append('</div>')
        md_lines.append("")

    md_lines.append('<hr style="border-top: 1px solid #f3f4f6; margin: 40px 0;">')
    md_lines.append("")
    md_lines.append("<h2 style=\"font-size: 1.8em; margin-bottom: 20px;\">Citation Profiles</h2>")
    md_lines.append("<ul style=\"font-size: 1.1em; line-height: 1.8;\">")
    if scholar_id:
        md_lines.append(f'<li><a href="https://scholar.google.com/citations?user={scholar_id}">Google Scholar</a></li>')
    else:
        md_lines.append('<li><a href="https://scholar.google.com/citations?user=YOUR_ID">Google Scholar</a></li>')
    md_lines.append('<li><a href="https://www.researchgate.net/profile/Nicolas-Leins?ev=hdr_xprf">ResearchGate</a></li>')
    md_lines.append("</ul>")
    md_lines.append("")

    return '\n'.join(md_lines)


def main():
    """Main function."""
    # Read BibTeX file
    bib_file = Path("Personal Publications.bib")

    if not bib_file.exists():
        print(f"Error: {bib_file} not found!")
        return

    print(f"Reading {bib_file}...")
    bib_content = bib_file.read_text(encoding='utf-8')

    # Parse entries
    print("Parsing BibTeX entries...")
    entries = parse_bibtex(bib_content)
    print(f"Found {len(entries)} entries")

    # Load optional Scholar ID from _config.yml
    scholar_id = None
    config_file = Path("_config.yml")
    if config_file.exists():
        config_text = config_file.read_text(encoding='utf-8')
        match = re.search(r'^\s*scholar_userid:\s*(.+)\s*$', config_text, flags=re.MULTILINE)
        if match:
            scholar_id = match.group(1).strip().strip('"').strip("'")

    # Generate markdown
    print("Generating publications.md...")
    md_content = generate_publications_md(entries, scholar_id=scholar_id)

    # Write to file
    output_file = Path("publications.md")
    output_file.write_text(md_content, encoding='utf-8')
    print(f"✓ Created {output_file}")
    print("\nDone! Your publications page has been updated.")


if __name__ == "__main__":
    main()
