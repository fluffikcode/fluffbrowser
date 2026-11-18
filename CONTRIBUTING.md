# Contributing to FluffBrowser

Thanks for wanting to make the fluff fluffier. This guide is short on purpose.

## Ways to help

- 🐛 Report a bug with the [bug template](.github/ISSUE_TEMPLATE/bug_report.yml)
- 💡 Suggest a feature with the [feature template](.github/ISSUE_TEMPLATE/feature_request.yml)
- 🎨 Improve the palette, logo or wording
- 🌍 Translate `fluffbrowser/ui/strings.py`
- 📖 Fix docs, add examples
- 🔧 Send a pull request

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
python -m playwright install chromium
python startbrowser.py
```

You need a reachable OpenAI-compatible endpoint to exercise real tasks. A local LM Studio or
Ollama model is enough; see [docs/QUICKSTART.md](docs/QUICKSTART.md).

## Before you open a PR

```bash
ruff check .                       # lint
python -m compileall fluffbrowser startbrowser.py
python -m unittest discover -s tests   # unit tests (stdlib only)
python startbrowser.py             # smoke test the UI
```

- Keep the design language intact unless the PR is explicitly about design.
- Put new user-facing text in `fluffbrowser/ui/strings.py`.
- Put new colours in `fluffbrowser/theme.py`.
- Never commit keys, `.env`, browser profiles or logs.
- Keep lines under 100 characters; the CI enforces ruff with `E`, `F`, `I`, `UP`, `B`, `SIM`.

## Commit messages

Conventional-ish, short, imperative:

```text
feat: add headless toggle to config
fix: close browser when startup fails
docs: explain .env precedence
style: soften error panel border
```

## Project values

1. **Calm over loud.** No flashing, no noise, no emoji soup in the interface.
2. **Small files.** If a module grows past ~200 lines, it probably wants to be two.
3. **No surprises.** Every action is visible in the browser window.
4. **No secrets.** Configuration is layered so nobody has to commit a key.

## Code of conduct

Be kind, assume good faith, critique code rather than people. Maintainers may close
contributions that ignore these basics.
