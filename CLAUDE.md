# CLAUDE.md — LHSOM Sheet Music Catalog

Guidance for any AI agent (Claude Code, or another model via a launcher) working in this repo.

> **This is a PUBLIC repository.** Keep it free of personal, private, or institution-sensitive
> content. Do not reference private infrastructure, personal notes, or non-public data here.

## Automation & non-primary AI sessions (review-gated)

This repo is a **public product maintained from a private hub**, so all changes here are
**review-gated** — a maintainer reviews and publishes them.

### Which kind of session am I?

You are a **non-primary session** if you are an AI agent driven by a non-Anthropic model through
a launcher, rather than the maintainer's own primary Claude. If your session was started by a
model launcher rather than by the maintainer directly, treat yourself as non-primary. The
maintainer's hub documents the exact environment markers, and the git guard detects them
automatically.

### If you are non-primary: drafts only

**Do your work in the working tree, then stop. Never `git commit`, and never `git push`.**
A guard blocks **both** commit and push and exits non-zero — it is not push-only. A primary
Anthropic session is the **sole committer of record**, and this note is the intent behind that
block, not a way around it.

Three rules, each of which exists because it was broken on 2026-08-20:

1. **Do not run `git add`.** "Staging" here means the **git index** and nothing else. It does
   *not* mean "prepare your work" — preparing your work for the primary is the whole point of your
   session, and you do it by leaving your edits in the working tree and writing a clear account in
   the daily log (rule 3). What `git add` does is freeze a snapshot in the index; if you keep
   editing afterwards, the index and the working tree drift apart, `git status` shows `AM`/`MM`,
   and a primary who commits the index captures **less than you actually did**. On 2026-08-20 that
   gap was 201 lines, including an entire section of the session's work.
2. **Never report a commit you did not make.** If the guard blocked you, say so plainly. A driver
   session reported four local commits that did not exist, and reported deleting files that were
   still present.
3. **Write your account where the primary will find it.** Append a `## <Model> Session` entry to
   `agent/memory-short-term/daily/YYYY-MM-DD.md`. If a driver stub file for today exists, write
   there instead. If you write anywhere else, say so in the stub — a primary who finds an empty
   stub will otherwise conclude you did nothing.

### If you are primary: reconcile before you start

Uncommitted edits here are non-primary drafts, because a non-primary cannot have committed.

- **Detect.** Run `git status` in **every** repo the driver may have touched, not only the one
  holding a stub, and read the main `daily/<date>.md` as well as the stub. An `AM` or `MM` status
  code means the working tree holds more than the index: commit the working tree.
- **Verify, don't trust.** Non-primary models botch tasks, ignore protocol, and fabricate.
  Spot-check the diff and every factual claim before accepting any of it.
- **Resolve.** Accept (stage by name and commit as the primary, attributing the driver), fix, or
  discard. Correct a false claim in the draft log in place, marking the correction, rather than
  silently rewriting it.
- **Fold before deleting.** Remove a driver stub only once its account is folded into the primary
  log, and only when the maintainer says so.

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
