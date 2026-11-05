# Contributing to The CMP Branch — RISC OS News

Thank you for contributing to the RISC OS community news site! This guide explains how to submit articles and what to expect during the review process.

## How to Contribute

### Types of Contributions Welcome

- **News articles** about RISC OS software, hardware, events, or community developments
- **Announcements** of new releases or updates
- **Event coverage** for meetups, shows, or online gatherings
- **Corrections** to existing articles (via PR)
- **Site improvements** (bug fixes, styling, features)

### What We Don't Accept

- Opinion pieces or editorials (this is a news site)
- Unverified rumors or speculation
- Commercial advertising disguised as news
- Off-topic content unrelated to RISC OS
- Duplicate articles already covered

## Submission Process

### 1. Prepare Your Article

Create a new Markdown file following the naming convention:

```
YYYY-MM-DD-article-title.md
```

Example: `2026-11-05-new-riscos-browser-released.md`

### 2. Format Your Article

Use this template:

```markdown
---
layout: post
title: "Your Article Title Here"
date: 2026-11-05 14:30:00 +0000
summary: "A one-sentence summary that will appear on the homepage."
tags: [relevant, tags, here]
source_url: "https://example.com/original-announcement"
source_name: "Example Site Name"
---

Write your article content here in Markdown.

## Headings Work

You can use standard Markdown formatting:

- Lists
- **Bold** and *italic* text
- [Links](https://example.com)
- Code blocks

Remember to credit sources if you're sharing news from elsewhere.
```

### 3. Fork and Create a Branch

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/News.git
cd News
git checkout -b add-article-descriptive-name

# Add your article file to _posts/
# Then:
git add _posts/2026-11-05-your-article.md
git commit -m "Add article: Your Article Title"
git push origin add-article-descriptive-name
```

### 4. Open a Pull Request

1. Go to the main repository: https://github.com/The-CMP-Branch/News
2. Click **"Pull requests"** → **"New pull request"**
3. Click **"compare across forks"**
4. Select your fork and branch
5. Fill in the PR template:
   - **Title**: "Add article: [Article Title]"
   - **Description**: Briefly explain the article and its source
6. Submit the PR

### 5. Review Process

**What happens next:**

1. **Automated checks**: Jekyll will attempt to build the site with your article
2. **Maintainer review**: A maintainer will review your article for:
   - Accuracy and verifiability
   - Proper formatting and front matter
   - Appropriate sourcing and credits
   - Relevance to RISC OS community
3. **Feedback**: You may be asked to make revisions
4. **Merge**: Once approved, your PR is merged to `main`
5. **Deployment**: GitHub Pages automatically rebuilds and deploys (1-2 minutes)

**Review timeline:** Most articles are reviewed within 48 hours.

## Article Guidelines

### Front Matter Requirements

| Field | Required? | Notes |
|-------|-----------|-------|
| `layout` | **Yes** | Always `post` |
| `title` | **Yes** | Clear, descriptive headline |
| `date` | **Yes** | Use article's original publication date when applicable |
| `summary` | **Strongly recommended** | 1-2 sentences for homepage preview |
| `tags` | Optional | Use existing tags when possible: `software`, `hardware`, `community`, `events`, `development` |
| `source_url` | When sharing news | Link to original announcement/article |
| `source_name` | When sharing news | Name of the source site |

### Content Best Practices

#### DO:
- ✅ Verify facts before submitting
- ✅ Credit original sources with `source_url` and `source_name`
- ✅ Write in clear, neutral language
- ✅ Use proper Markdown formatting
- ✅ Check spelling and grammar
- ✅ Include relevant links
- ✅ Focus on factual information

#### DON'T:
- ❌ Copy entire articles verbatim (summarize and link instead)
- ❌ Add opinion or commentary (stick to facts)
- ❌ Use clickbait headlines
- ❌ Submit rumors or unverified information
- ❌ Forget to credit sources
- ❌ Include excessive formatting or styling

### Date Format

Always use this format for the `date` field:

```yaml
date: 2026-11-05 14:30:00 +0000
```

- **Date**: YYYY-MM-DD
- **Time**: HH:MM:SS (24-hour format)
- **Timezone**: +0000 (UTC) — convert if necessary

### Tags

Prefer existing tags to keep the site organized:

- `software` — Software releases, updates, apps
- `hardware` — Hardware announcements, devices
- `community` — Community news, discussions
- `events` — Meetups, conferences, shows
- `development` — Development tools, libraries
- `documentation` — Guides, tutorials, reference material

New tags are acceptable if none of the above fit.

## Code Contributions

Contributing site improvements? Great! Follow these guidelines:

### Setting Up Locally

```bash
git clone https://github.com/The-CMP-Branch/News.git
cd News

# Install Jekyll (requires Ruby)
gem install jekyll bundler

# Serve locally
jekyll serve

# Visit: http://localhost:4000/News/
```

### Making Changes

1. Create a descriptive branch: `git checkout -b fix-mobile-nav`
2. Make your changes
3. Test locally with `jekyll serve`
4. Commit with clear messages: `git commit -m "Fix mobile navigation menu"`
5. Push and open a PR

### Code Style

- **HTML/CSS**: Use clean, semantic HTML; keep CSS organized
- **Markdown**: Follow standard Markdown conventions
- **Jekyll**: Use Jekyll best practices and built-in features
- **Comments**: Comment complex logic; avoid obvious comments

## Questions?

- **Not sure if your article fits?** Open an issue to discuss first
- **Need help with Markdown?** See [Markdown Guide](https://www.markdownguide.org/)
- **Technical issues?** Open an issue with details

## Code of Conduct

Be respectful and constructive. This is a community resource:

- Be welcoming to newcomers
- Assume good faith
- Accept constructive feedback gracefully
- Focus on facts, not opinions
- Help maintain a positive community space

## License Note

By contributing, you agree that:

- Article content may be attributed to you or the original source
- Site code/templates contributions are freely usable by this project
- You have the right to share any content you submit

---

Thank you for helping build a valuable resource for the RISC OS community!
