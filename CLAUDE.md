# CLAUDE.md — LHSOM Sheet Music Catalog

Guidance for any AI agent (Claude Code, or another model via a launcher) working in this repo.

> **This is a PUBLIC repository.** Keep it free of personal, private, or institution-sensitive
> content. Do not reference private infrastructure, personal notes, or non-public data here.

## What this is

A digital catalog of sheet music held by the **Lionel Hampton School of Music (LHSOM)**,
University of Idaho — a static website built on **CollectionBuilder-Sheets** (a Jekyll template
for CSV-driven digital collections), deployed on **GitHub Pages**. No database, no backend: the
whole site is driven by CSV metadata.

- **Live site:** https://johnstonhorn.github.io/lhsom-sheetmusic-library/
- **Framework:** CollectionBuilder-Sheets — https://github.com/CollectionBuilder/collectionbuilder-sheets

## Structure

| Path | What it is |
|---|---|
| `data/` | the catalog metadata — one CSV per ensemble type + `entire_library.csv` (the master feed) |
| `_config.yml` | site settings; `metadata-csv:` names the master CSV; `baseurl:` **must** equal the repo name |
| `_data/config-*.csv` | which fields appear where (browse, table, search, metadata display) |
| `objects/` | branding (LHSOM logos) + any attached object files |
| `pages/` | site pages (browse, subjects, data, about) |
| `_layouts/ _includes/ _sass/ assets/` | CollectionBuilder theme internals — rarely edited |

## Local development

```bash
bundle install               # once — installs Jekyll + deps (needs Ruby + Bundler)
bundle exec jekyll serve     # preview at http://localhost:4000/lhsom-sheetmusic-library/
```

## Updating the catalog (the common task)

1. Edit the CSV(s) in `data/` — keep header names and column order consistent; UTF-8.
2. `entire_library.csv` is the master feed named in `_config.yml` (`metadata-csv:`).
3. Commit and push to `main`.
4. GitHub Pages rebuilds automatically — no manual deploy step.

**CSV rules CollectionBuilder expects:** UTF-8, a header row, consistent columns across all rows,
and (if attaching object files) a unique `objectid` per row. Strip empty trailing columns left by
Excel exports (e.g. `column_12`).

## Deployment

GitHub Pages builds from `main` on every push. If links break, first check that `baseurl` in
`_config.yml` still equals `/lhsom-sheetmusic-library`.

## Provenance

Adapted from the CollectionBuilder-Sheets template; took over from the original
`thecdil/music-library-demo` reference site. CollectionBuilder is a project of the University of
Idaho Library's Digital Initiatives and the Center for Digital Inquiry and Learning (CDIL).
