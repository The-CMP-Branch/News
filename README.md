# The CMP Branch — RISC OS News

A community news site for RISC OS, built with Jekyll and hosted on GitHub Pages.

**Live site:** https://the-cmp-branch.github.io/News/ (after Pages is enabled)

## About

This site curates news and updates from the RISC OS community, including:
- Software releases and updates
- Hardware announcements
- Community events and meetups
- Development news

All articles credit their original sources and are community-contributed via pull requests.

## Getting Started (For Site Administrators)

### Enable GitHub Pages

1. Go to **Settings** → **Pages** in this repository
2. Under "Build and deployment" → "Source", select **Deploy from a branch**
3. Select branch: **main** and folder: **/ (root)**
4. Click **Save**

GitHub will automatically build and deploy the site when changes are pushed to the main branch. The site typically takes 1-2 minutes to build and deploy.

### Local Development (Optional)

To preview the site locally before pushing:

```bash
# Install Ruby and Bundler if you haven't already
# Then install Jekyll:
gem install jekyll bundler

# Create a Gemfile (optional, for dependency management):
bundle init
bundle add jekyll

# Serve the site locally:
bundle exec jekyll serve

# Or if you installed Jekyll globally:
jekyll serve
```

Visit `http://localhost:4000/News/` in your browser to preview.

## Adding a News Article

### Quick Start

1. **Fork this repository** (or create a new branch if you have write access)
2. **Create a new Markdown file** in the `_posts/` directory
3. **Name it** using the format: `YYYY-MM-DD-article-title.md`
   - Example: `2026-11-05-risc-os-6-update.md`
4. **Add front matter** and content (see below)
5. **Submit a pull request** with your article
6. **Wait for review** — a maintainer will review and merge

### Article Format

Each article is a Markdown file with YAML front matter at the top. Here's the structure:

```markdown
---
layout: post
title: "Your Article Title"
date: 2026-11-05 14:30:00 +0000
summary: "A brief one-sentence summary of the article."
tags: [software, hardware, community, events]
source_url: "https://example.com/original-article"
source_name: "Original Website Name"
---

Your article content goes here in Markdown format.

## You Can Use Headings

- And lists
- Like this

Links work too: [RISC OS](https://www.riscosopen.org/)
```

### Front Matter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `layout` | Yes | Always set to `post` |
| `title` | Yes | The article headline |
| `date` | Yes | Publication date in `YYYY-MM-DD HH:MM:SS +0000` format |
| `summary` | Recommended | A brief summary (shows on the homepage) |
| `tags` | Optional | List of tags like `[software, community]` |
| `source_url` | When applicable | Link to the original article/announcement |
| `source_name` | When applicable | Name of the source website |
| `image` | Optional | Image path for social share previews (falls back to the site logo) |
| `image_alt` | With `image` | Short description of the share image |

### Content Guidelines

- **Credit sources**: If you're sharing news from another site, always include `source_url` and `source_name`
- **Be accurate**: Verify information before submitting
- **Stay on topic**: Focus on RISC OS-related news
- **Write clearly**: Use clear, community-friendly language
- **No opinions**: This is a news aggregation site, not an editorial platform

## Pull Request Workflow

All articles are reviewed before publication:

1. **Submit your PR** with the new article
2. **Maintainer reviews** for accuracy, formatting, and appropriateness
3. **Revisions if needed** — you may be asked to make changes
4. **Merge** — once approved, the PR is merged to `main`
5. **Automatic deployment** — GitHub Pages rebuilds the site automatically (1-2 minutes)

See [CONTRIBUTING.md](CONTRIBUTING.md) for more detailed contribution guidelines.

## File Structure

```
News/
├── _config.yml           # Jekyll configuration
├── _layouts/             # HTML templates
│   ├── default.html      # Base layout
│   └── post.html         # Article layout
├── _posts/               # News articles (Markdown files)
│   └── YYYY-MM-DD-title.md
├── assets/
│   └── css/
│       └── style.css     # Site styling
├── index.html            # Homepage (lists articles)
├── about.md              # About page
├── README.md             # This file
└── CONTRIBUTING.md       # Contribution guidelines
```

## Technology

- **Jekyll**: Static site generator (GitHub Pages native support)
- **Markdown**: Article format with YAML front matter
- **GitHub Pages**: Free hosting, automatic builds from `main` branch
- **No custom Actions required**: Jekyll is built-in to GitHub Pages

## Maintenance

### Common Tasks

**Adding a new tag:** Just use it in an article's front matter. Tags are automatically collected from articles.

**Changing the site title or description:** Edit `_config.yml`

**Updating styles:** Edit `assets/css/style.css`

**Modifying layouts:** Edit files in `_layouts/`

## Support

- **Questions?** Open an issue in this repository
- **Found a bug?** Open an issue with details
- **Want to contribute?** See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

Articles remain under their original licenses. Site code and templates are available for reuse by the RISC OS community.

---

Maintained by [The CMP Branch](https://github.com/The-CMP-Branch)
