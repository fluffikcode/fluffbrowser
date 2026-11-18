# Configuration

FluffBrowser has three configuration layers. Later layers win:

```text
startbrowser.py CONFIG block  →  .env file  →  FLUFFBROWSER_* environment variables
```

If you install the package and run `fluffbrowser`, the first layer does not exist and the app
starts from built-in defaults (placeholder key, LM Studio URL).

## The CONFIG block

```python
BASE_URL = "http://localhost:1234/v1"
API_KEY = "your-api-key"
MODEL = "your-model-name"

TEMPERATURE = 0.0
MAX_STEPS = 15
TASK_TIMEOUT = 600
HEADLESS = False
BROWSER_TYPE = "chromium"
```

| Name | Type | Default | Notes |
| --- | --- | --- | --- |
| `BASE_URL` | `str` | `http://localhost:1234/v1` | Must start with `http://` or `https://`; keep the `/v1` suffix |
| `API_KEY` | `str` | `your-api-key` | Placeholder values trigger a friendly warning, not a crash |
| `MODEL` | `str` | `your-model-name` | Exactly as your server reports it; must support tool calling |
| `TEMPERATURE` | `float` | `0.0` | `0.0` for repeatable browsing, `0.3–0.7` for creative research |
| `MAX_STEPS` | `int` | `15` | Each click/keystroke/navigation counts as a step |
| `TASK_TIMEOUT` | `int` | `600` | Seconds per task before it is aborted |
| `HEADLESS` | `bool` | `False` | `True` for servers / CI (you lose the show) |
| `BROWSER_TYPE` | `str` | `chromium` | `chromium` or `chrome` (browser-use 1.x kinds) |

## Environment variables

Every setting has an env-var twin with the `FLUFFBROWSER_` prefix:

| Variable | Setting |
| --- | --- |
| `FLUFFBROWSER_BASE_URL` | `BASE_URL` |
| `FLUFFBROWSER_API_KEY` | `API_KEY` |
| `FLUFFBROWSER_MODEL` | `MODEL` |
| `FLUFFBROWSER_TEMPERATURE` | `TEMPERATURE` |
| `FLUFFBROWSER_MAX_STEPS` | `MAX_STEPS` |
| `FLUFFBROWSER_TIMEOUT` | `TASK_TIMEOUT` |
| `FLUFFBROWSER_HEADLESS` | `HEADLESS` |
| `FLUFFBROWSER_BROWSER_TYPE` | `BROWSER_TYPE` |

Booleans accept `1/true/yes/y/on`. Invalid numbers are ignored (the previous value survives),
so a typo never bricks startup.

```powershell
$env:FLUFFBROWSER_MODEL = "qwen2.5-7b-instruct"
run.bat
```

```bash
FLUFFBROWSER_MODEL=qwen2.5:7b python startbrowser.py
```

## The `.env` file

```bash
copy .env.example .env
```

```dotenv
# comments and blank lines are fine
FLUFFBROWSER_BASE_URL=https://openrouter.ai/api/v1
FLUFFBROWSER_API_KEY=sk-or-v1-...
FLUFFBROWSER_MODEL=anthropic/claude-3.5-sonnet
```

Details:

- it is read from the current directory **and** from the project root;
- quoted values (`KEY="value"`), `export KEY=value` and `#` comments are supported;
- values never override variables already present in your shell.

## Privacy

FluffBrowser has no analytics of its own. `browser-use` sends anonymised statistics by default;
turn them off with a plain env var in the same `.env` (it is read by the library, not by
FluffBrowser):

```dotenv
ANONYMIZED_TELEMETRY=false
```

## Restyling

- Palette: `fluffbrowser/theme.py` — six hex colours.
- Logo: `fluffbrowser/assets/logo.txt` (any monospace ASCII art; `█` is highlighted, box-drawing
  characters get the shadow colour).
- Wording: `fluffbrowser/ui/strings.py` — every visible string, in one file.
- Screens: `fluffbrowser/ui/screens.py` — layouts, panels, prompts.

## Browser data

`browser-use` keeps its profile in your user directory (cookies, logins, history persist between
runs). For a disposable profile, pass `user_data_dir=` when constructing the browser in
`fluffbrowser/core/browser.py`, or set `BROWSER_TYPE = "chrome"` to drive your installed Chrome.
Project-local folders such as `browser_profile/`, `logs/` and `screenshots/` are git-ignored.
