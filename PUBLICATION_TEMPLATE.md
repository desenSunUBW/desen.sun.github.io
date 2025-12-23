# Publication Markdown Template Guide

This guide shows you how to manually create publication markdown files for your Academic Pages website.

## File Naming Convention

Files should be named: `YYYY-MM-DD-url-slug.md`

- **YYYY-MM-DD**: Publication date (year-month-day)
- **url-slug**: URL-friendly version of the title (lowercase, hyphens instead of spaces)

Example: `2024-03-15-efficient-diffusion-models.md`

## Markdown File Format

Here's the complete template:

```markdown
---
title: "Your Paper Title Here"
collection: publications
category: manuscripts  # Options: "manuscripts", "conferences", or "books"
permalink: /publication/2024-03-15-your-paper-title
excerpt: 'Brief description or abstract of your paper (optional but recommended).'
date: 2024-03-15
venue: 'Journal or Conference Name'
paperurl: 'https://doi.org/your-doi-or-url'  # Optional: link to paper
slidesurl: 'https://example.com/slides.pdf'  # Optional: link to slides
codeurl: 'https://github.com/your-repo'      # Optional: link to code
citation: 'Author1, A., Author2, B., & Sun, D. (2024). &quot;Your Paper Title.&quot; <i>Journal Name</i>. 1(1), 1-10.'
---

<a href='https://doi.org/your-doi-or-url'>Download paper here</a>

Your detailed description, abstract, or additional information about the paper goes here. This will be displayed on the individual publication page.

Recommended citation: Author1, A., Author2, B., & Sun, D. (2024). "Your Paper Title." <i>Journal Name</i>. 1(1), 1-10.
```

## Field Descriptions

### Required Fields:
- **title**: Full title of your paper (use quotes)
- **collection**: Always `publications`
- **category**: 
  - `manuscripts` for journal articles
  - `conferences` for conference papers
  - `books` for books/book chapters
- **permalink**: URL path (format: `/publication/YYYY-MM-DD-url-slug`)
- **date**: Publication date (format: `YYYY-MM-DD`)
- **venue**: Journal or conference name
- **citation**: Full citation in HTML format (use `&quot;` for quotes, `<i>` for italics)

### Optional Fields:
- **excerpt**: Short description (appears in publication list)
- **paperurl**: Link to paper (DOI, arXiv, PDF, etc.)
- **slidesurl**: Link to presentation slides
- **codeurl**: Link to code repository

## Category Examples

### Journal Article (manuscripts):
```yaml
category: manuscripts
venue: 'IEEE Transactions on Machine Learning'
```

### Conference Paper (conferences):
```yaml
category: conferences
venue: 'NeurIPS 2024'
```

### Book Chapter (books):
```yaml
category: books
venue: 'Advances in Machine Learning'
```

## Citation Format

The citation should be in HTML format. Here's an example:

```yaml
citation: 'Sun, D., Liu, S., & Zhang, J. (2024). &quot;Efficient and Secure Diffusion Models.&quot; <i>ICML 2024</i>. 1-15.'
```

**Important HTML entities:**
- Use `&quot;` for double quotes around titles
- Use `<i>...</i>` for italic text (journal/conference names)
- Use `&amp;` for ampersands (&)

## Example: Complete Publication File

```markdown
---
title: "Efficient and Secure Diffusion Models for Image Generation"
collection: publications
category: conferences
permalink: /publication/2024-06-15-efficient-secure-diffusion
excerpt: 'We propose a novel approach to improve both efficiency and security of diffusion models through architectural optimizations and privacy-preserving mechanisms.'
date: 2024-06-15
venue: 'International Conference on Machine Learning (ICML)'
paperurl: 'https://arxiv.org/abs/2024.12345'
codeurl: 'https://github.com/desenSunUBW/efficient-diffusion'
citation: 'Sun, D., Liu, S., & Bai, Y. (2024). &quot;Efficient and Secure Diffusion Models for Image Generation.&quot; <i>ICML 2024</i>. 1-15.'
---

<a href='https://arxiv.org/abs/2024.12345'>Download paper here</a>

Diffusion models have shown remarkable success in generative tasks, but face challenges in computational efficiency and security. In this work, we propose...

**Key Contributions:**
- Accelerated sampling algorithms reducing steps by 50%
- Privacy-preserving training mechanisms
- Robustness against adversarial attacks

Recommended citation: Sun, D., Liu, S., & Bai, Y. (2024). "Efficient and Secure Diffusion Models for Image Generation." <i>ICML 2024</i>. 1-15.
```

## Quick Steps to Add a Publication

1. **Create a new file** in `_publications/` folder
2. **Name it**: `YYYY-MM-DD-your-title-slug.md`
3. **Copy the template** above
4. **Fill in your information**
5. **Save the file**
6. **Test locally** with `jekyll serve` to see it on your publications page

## Tips

- Keep the **url-slug** short and descriptive (use hyphens, no spaces)
- The **date** should match when the paper was published/accepted
- **Excerpt** should be 1-2 sentences summarizing the paper
- Use **paperurl** for DOI links, arXiv links, or direct PDF links
- The main content (below `---`) can include markdown formatting, images, etc.

## Editing Existing Files

You can edit any of the example files in `_publications/`:
- `2009-10-01-paper-title-number-1.md`
- `2010-10-01-paper-title-number-2.md`
- `2015-10-01-paper-title-number-3.md`
- `2024-02-17-paper-title-number-4.md`
- `2025-06-08-paper-title-number-5.md`

Just replace the content with your publication information!

