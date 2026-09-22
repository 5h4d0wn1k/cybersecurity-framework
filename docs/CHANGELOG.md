# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- `scripts/build.py`: validate tool URLs are `http(s)`, tolerate non-numeric
  ratings, add `--ci` mode that fails on any validation warning or drift from
  committed output, regenerate `docs/sitemap.xml` (deduplicated, `lastmod`
  from last commit), and stop double-mirroring markdown into `docs/data/`.

### Security
- Runtime URL guard in `docs/index.html`: tool links and `window.open` only
  accept `https?://` schemes (defense-in-depth alongside build-time checks).

### Fixed
- Panel focus is only taken over on keyboard activation; mouse/touch opening
  no longer steals focus, and every close path restores it.
- Branch toggle feedback (`.pulse`) is no longer wiped by re-render.
- Keyboard `ArrowRight` no longer crashes on childless leaf nodes; malformed
  `tree.json` payloads and non-array `alt` fields are rejected safely.
- Fast mouse double-clicks no longer trigger touch double-tap logic (now
  gated to touch-capable narrow viewports).
- Node pills are only rebuilt when their content actually changes (render
  performance), and the tooltip hint no longer uses a hardcoded offset.

## [2026-09-22]

### Added
- Full public launch: `VISION.md`, `SCOPE.md`, `SCHEMA.md`, `ETHICS.md`,
  `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE`,
  issue/PR templates, SEO `<head>` (JSON-LD, canonical, Open Graph,
  `robots.txt`, `sitemap.xml`), and `docs/` build mirror.
- Interactive tree with search (name/path/description), reveal & highlight,
  panel detail with install/alternatives and copy button, theme toggle,
  domain jump box, and expand/collapse of the full 27-domain / 776-category
  / 1067-tool graph.

### Fixed
- Full-page dot grid placement and 20 audit-driven UI fixes.

### Changed
- `docs/index.html` runs entirely client-side against `docs/data/tree.json`
  generated deterministically by `scripts/build.py`.