# Adding Publications from Google Scholar

This guide will help you add your publications from Google Scholar to your Academic Pages website.

## Step 1: Export from Google Scholar

1. Go to your Google Scholar profile: https://scholar.google.com/citations?user=32CXyUYAAAAJ
2. Click the **"Export"** button (usually at the top right)
3. Select **"BibTeX"** format
4. Save the file as `scholar.bib` in the root directory of your website

## Step 2: Convert BibTeX to Markdown

You have two options:

### Option A: Use the existing script (requires pybtex)

1. Install pybtex if you don't have it:
   ```bash
   pip install pybtex
   ```

2. Place your `scholar.bib` file in the `markdown_generator` folder

3. Edit `markdown_generator/pubsFromBib.py` and update the `publist` dictionary:
   ```python
   publist = {
       "journal": {
           "file": "scholar.bib",  # Your BibTeX file
           "venuekey": "journal",
           "venue-pretext": "",
           "collection": {"name": "publications", "permalink": "/publication/"}
       },
       "conference": {
           "file": "scholar.bib",
           "venuekey": "booktitle",
           "venue-pretext": "In the proceedings of ",
           "collection": {"name": "publications", "permalink": "/publication/"}
       }
   }
   ```

4. Run the script:
   ```bash
   cd markdown_generator
   python pubsFromBib.py
   ```

### Option B: Use the simple conversion script

1. Place your `scholar.bib` file in the root directory

2. Run the conversion script:
   ```bash
   python scripts/bibtex_to_publications.py scholar.bib
   ```

This will create markdown files in the `_publications` folder.

## Step 3: Review and Customize

After conversion, review the generated markdown files in `_publications/`:
- Check that titles, venues, and citations are correct
- Add or update excerpts/abstracts if needed
- Verify paper URLs (DOI links, arXiv links, etc.)
- Update categories if needed (manuscripts, conferences, books)

## Step 4: Clean Up

Remove the example publication files if desired:
- `2009-10-01-paper-title-number-1.md`
- `2010-10-01-paper-title-number-2.md`
- `2015-10-01-paper-title-number-3.md`
- `2024-02-17-paper-title-number-4.md`
- `2025-06-08-paper-title-number-5.md`

## Manual Entry (Alternative)

If you prefer to add publications manually, create markdown files in `_publications/` following this format:

```markdown
---
title: "Your Paper Title"
collection: publications
category: manuscripts  # or "conferences" or "books"
permalink: /publication/2024-01-15-your-paper-title
excerpt: 'Brief description of your paper.'
date: 2024-01-15
venue: 'Journal or Conference Name'
paperurl: 'https://doi.org/your-doi-or-url'
citation: 'Author1, A., Author2, B., & You, D. (2024). &quot;Your Paper Title.&quot; <i>Journal Name</i>. 1(1), 1-10.'
---

<a href='https://doi.org/your-doi-or-url'>Download paper here</a>

Your paper abstract or description here.

Recommended citation: Author1, A., Author2, B., & You, D. (2024). "Your Paper Title." <i>Journal Name</i>. 1(1), 1-10.
```

## Troubleshooting

- **Missing publications**: Check that your BibTeX export includes all publications
- **Incorrect formatting**: Manually edit the markdown files to fix any issues
- **Missing categories**: Update the `category` field (manuscripts, conferences, or books)
- **Broken links**: Verify paper URLs are correct and accessible

