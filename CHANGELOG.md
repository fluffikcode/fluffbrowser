# Changelog

All notable changes to FluffBrowser are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — 2026-11-18

### Added

- Package structure: `fluffbrowser/` with `config`, `theme`, `core/` and `ui/` modules.
- `.env` support and `FLUFFBROWSER_*` environment overrides — keys stay out of git.
- Friendly configuration warning panel instead of a silent failure with placeholder keys.
- `run.bat --update` to refresh dependencies inside an existing virtual environment.
- `run.bat` bootstrap: finds Python even outside PATH, creates `.venv`, installs
  requirements, downloads Chromium and remembers that it did.
- UTF-8 safe console output (`chcp 65001` + stream reconfiguration) so the logo survives
  legacy code pages and redirected output.
- `fluffbrowser` console command and `python -m fluffbrowser` entry point.
- Documentation: quickstart, configuration reference, architecture, troubleshooting,
  publishing guide.
- GitHub extras: CI workflow, Dependabot, issue/PR templates, contribution and security
  guides, editor config.
- `.gitignore`, `.gitattributes`, `.env.example`, MIT license, changelog.
- Stdlib unit tests for the configuration layer.

### Changed

- All user-facing text moved to `ui/strings.py`; colours to `theme.py`; logo to
  `fluffbrowser/assets/logo.txt`.
- Welcome-screen subtitle is now version-driven instead of hard-coding a model name.
- Browser creation tolerates several `browser-use` API shapes.
- Errors during startup are shown as a themed panel rather than a traceback.
- `Ctrl+Z` / EOF now exits cleanly, like `Ctrl+C`.
- Requirements now pin `browser-use>=1.0` and declare `playwright` explicitly, so Chromium
  can be installed without the optional `uv` toolchain.

### Removed

- Hard-coded endpoint URL, API key and model id from the source.

### Unchanged

- The visual design: palette, 3D ASCII logo, panels, spinners and layout.

## [1.0.0]

### Added

- Initial single-file FluffBrowser: beige terminal interface, persistent Chromium session,
  free-form tasks executed by a `browser-use` agent.
