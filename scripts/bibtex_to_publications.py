#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert BibTeX file to Academic Pages publication markdown files.
Usage: python bibtex_to_publications.py input.bib
"""

import re
import sys
import os
from datetime import datetime
from pathlib import Path

def html_escape(text):
    """Escape special characters for HTML/YAML."""
    if not text:
        return ""
    html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;"
    }
    return "".join(html_escape_table.get(c, c) for c in str(text))

def parse_bibtex_entry(entry_text):
    """Parse a single BibTeX entry."""
    entry = {}
    
    # Extract entry type and key
    type_match = re.search(r'@(\w+)\{([^,]+),', entry_text)
    if type_match:
        entry['type'] = type_match.group(1)
        entry['key'] = type_match.group(2)
    
    # Extract fields
    fields = {
        'title': r'title\s*=\s*[{"]([^}"]+)[}"]',
        'author': r'author\s*=\s*[{"]([^}"]+)[}"]',
        'journal': r'journal\s*=\s*[{"]([^}"]+)[}"]',
        'booktitle': r'booktitle\s*=\s*[{"]([^}"]+)[}"]',
        'year': r'year\s*=\s*[{"]([^}"]+)[}"]',
        'pages': r'pages\s*=\s*[{"]([^}"]+)[}"]',
        'volume': r'volume\s*=\s*[{"]([^}"]+)[}"]',
        'number': r'number\s*=\s*[{"]([^}"]+)[}"]',
        'url': r'url\s*=\s*[{"]([^}"]+)[}"]',
        'doi': r'doi\s*=\s*[{"]([^}"]+)[}"]',
        'abstract': r'abstract\s*=\s*[{"]([^}"]+)[}"]',
    }
    
    for field, pattern in fields.items():
        match = re.search(pattern, entry_text, re.IGNORECASE)
        if match:
            entry[field] = match.group(1).strip()
    
    return entry

def determine_category(entry_type, venue):
    """Determine publication category based on type and venue."""
    entry_type_lower = entry_type.lower()
    venue_lower = venue.lower() if venue else ""
    
    if entry_type_lower in ['inproceedings', 'conference']:
        return 'conferences'
    elif entry_type_lower in ['article', 'journal']:
        return 'manuscripts'
    elif entry_type_lower in ['book', 'inbook']:
        return 'books'
    else:
        return 'manuscripts'  # default

def format_citation(entry):
    """Format a citation string from entry data."""
    authors = entry.get('author', 'Unknown')
    title = entry.get('title', 'Untitled')
    venue = entry.get('journal') or entry.get('booktitle', 'Unknown Venue')
    year = entry.get('year', 'Unknown Year')
    
    # Clean up authors (remove braces, handle "and")
    authors = authors.replace('{', '').replace('}', '')
    if ' and ' in authors:
        author_list = authors.split(' and ')
        if len(author_list) > 3:
            authors = author_list[0] + ' et al.'
        else:
            authors = ', '.join(author_list[:-1]) + ' and ' + author_list[-1]
    
    citation = f'{authors}. ({year}). &quot;{title}.&quot; <i>{venue}</i>.'
    
    if entry.get('volume'):
        citation += f' {entry["volume"]}'
    if entry.get('number'):
        citation += f'({entry["number"]})'
    if entry.get('pages'):
        citation += f', {entry["pages"]}'
    citation += '.'
    
    return citation

def create_url_slug(title):
    """Create a URL-friendly slug from title."""
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '-', slug)
    slug = slug[:50]  # Limit length
    return slug.strip('-')

def create_markdown_file(entry, output_dir):
    """Create a markdown file for a publication entry."""
    year = entry.get('year', '2024')
    month = '01'  # Default to January if not specified
    day = '01'
    
    # Try to extract month if available
    date_str = f"{year}-{month}-{day}"
    
    title = entry.get('title', 'Untitled')
    url_slug = create_url_slug(title)
    filename = f"{date_str}-{url_slug}.md"
    filepath = os.path.join(output_dir, filename)
    
    # Determine category
    venue = entry.get('journal') or entry.get('booktitle', '')
    category = determine_category(entry.get('type', 'article'), venue)
    
    # Build markdown content
    md = "---\n"
    md += f'title: "{html_escape(title)}"\n'
    md += "collection: publications\n"
    md += f"category: {category}\n"
    md += f"permalink: /publication/{date_str}-{url_slug}\n"
    
    if entry.get('abstract'):
        excerpt = entry['abstract'][:200] + "..." if len(entry['abstract']) > 200 else entry['abstract']
        md += f"excerpt: '{html_escape(excerpt)}'\n"
    
    md += f"date: {date_str}\n"
    md += f"venue: '{html_escape(venue)}'\n"
    
    # Add paper URL (DOI or URL)
    paperurl = entry.get('url') or (f"https://doi.org/{entry['doi']}" if entry.get('doi') else '')
    if paperurl:
        md += f"paperurl: '{paperurl}'\n"
    
    # Create citation
    citation = format_citation(entry)
    md += f"citation: '{html_escape(citation)}'\n"
    md += "---\n\n"
    
    # Add content
    if paperurl:
        md += f"<a href='{paperurl}'>Download paper here</a>\n\n"
    
    if entry.get('abstract'):
        md += f"{entry['abstract']}\n\n"
    
    md += f"Recommended citation: {citation}\n"
    
    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)
    
    print(f"Created: {filename}")
    return filename

def main():
    if len(sys.argv) < 2:
        print("Usage: python bibtex_to_publications.py <input.bib>")
        print("\nTo export from Google Scholar:")
        print("1. Go to https://scholar.google.com/citations?user=32CXyUYAAAAJ")
        print("2. Click 'Export' and select 'BibTeX'")
        print("3. Save the file and run this script")
        sys.exit(1)
    
    bib_file = sys.argv[1]
    if not os.path.exists(bib_file):
        print(f"Error: File '{bib_file}' not found")
        sys.exit(1)
    
    # Output directory
    output_dir = Path(__file__).parent.parent / '_publications'
    output_dir.mkdir(exist_ok=True)
    
    # Read BibTeX file
    with open(bib_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into entries
    entries = re.split(r'@\w+\{', content)
    entries = [entry for entry in entries if entry.strip()]
    
    print(f"Found {len(entries)} entries in BibTeX file\n")
    
    # Process each entry
    for i, entry_text in enumerate(entries, 1):
        if not entry_text.strip():
            continue
        
        # Add back the @type{key, part
        entry_text = '@' + entry_text
        
        try:
            entry = parse_bibtex_entry(entry_text)
            if entry.get('title'):
                create_markdown_file(entry, str(output_dir))
            else:
                print(f"Skipping entry {i}: No title found")
        except Exception as e:
            print(f"Error processing entry {i}: {e}")
            continue
    
    print(f"\nDone! Created publication markdown files in {output_dir}")

if __name__ == '__main__':
    main()

