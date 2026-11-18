<div align="center">

```
███████╗██╗     ██╗   ██╗███████╗███████╗██████╗ ██████╗  ██████╗ ██╗    ██╗███████╗███████╗██████╗
██╔════╝██║     ██║   ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔════╝██╔══██╗
█████╗  ██║     ██║   ██║█████╗  █████╗  ██████╔╝██████╔╝██║   ██║██║ █╗ ██║███████╗█████╗  ██████╔╝
██╔══╝  ██║     ██║   ██║██╔══╝  ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██║███╗██║╚════██║██╔══╝  ██╔══██╗
██║     ███████╗╚██████╔╝██║     ██║     ██████╔╝██║  ██║╚██████╔╝╚███╔███╔╝███████║███████╗██║  ██║
╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝
```

**Talk to your browser. It does the clicking.**

A calm, cream-and-bronze terminal cockpit for an AI agent that drives a real Chromium window.

[![Python](https://img.shields.io/badge/python-3.11%2B-9C7A54?style=flat-square)](pyproject.toml)
[![License: MIT](https://img.shields.io/badge/license-MIT-A3B18A?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-D5BDAF?style=flat-square)](#requirements)
[![Powered by browser-use](https://img.shields.io/badge/powered%20by-browser--use-9C7A54?style=flat-square)](https://github.com/browser-use/browser-use)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-C97A7A?style=flat-square)](CONTRIBUTING.md)

</div>

---

## ✨ What is FluffBrowser?

You write a task in plain language — *"find the cheapest direct flight to Lisbon next Friday"* —
and an LLM agent works through it inside a visible Chromium window: it opens pages, types,
clicks, scrolls, reads and retries. The answer comes back as a tidy Markdown card right in
your terminal.

- 🍦 **Calm by design** — beige palette, 3D ASCII logo, zero visual noise.
- 🧠 **Any OpenAI-compatible model** — LM Studio, Ollama, vLLM, llama.cpp, OpenAI, OpenRouter…
- 👀 **Visible browser** — you watch every action, so nothing happens behind your back.
- 🔁 **Stay in flow** — ask again, `clear`, `exit`; one persistent browser session per run.
- 🔒 **Private by default** — your endpoint, your key, your machine; no accounts and no analytics
  of our own (third-party `browser-use` telemetry is one line away from being off).
- 🧩 **Small, readable code** — a clean package split, easy to fork and restyle.

## ⚡ Quick start (2 steps)

### 1. Point FluffBrowser at your model

Open **`startbrowser.py`** and edit the CONFIG block at the top:

```python
BASE_URL = "http://localhost:1234/v1"  # your OpenAI-compatible endpoint
API_KEY = "your-api-key"               # LM Studio/Ollama: any value works
MODEL = "your-model-name"              # e.g. "qwen2.5-7b-instruct"
```

### 2. Run the batch file

Double-click **`run.bat`**.

The first launch creates `.venv`, installs the dependencies and downloads Chromium.
Every launch after that starts straight away.

> **Prefer not to touch the file?** Copy `.env.example` to `.env`, fill in the three
> values, and FluffBrowser picks them up automatically — the file is ignored by git.

That's it. Type a task, watch the browser, read the answer.

```text
╭─ ✦ Вы
╰─▸ открой news.ycombinator.com и покажи три верхние темы
```

## 🧾 Commands

| Command | What it does |
| --- | --- |
| *(any text)* | Hand the task to the agent |
| `clear` / `очистить` / `cls` | Repaint the start screen |
| `exit` / `выход` / `quit` / `q` | Close the browser and leave |
| `Ctrl+C` | Stop the current task and shut down |

## ✅ Requirements

- **Python 3.11+** (3.12 or 3.13 recommended)
- **Windows 10/11** for `run.bat`; macOS/Linux work with the manual commands
- An **OpenAI-compatible LLM endpoint** whose model supports **tool calling**
  (agents need it to click and type)
No endpoint yet? [docs/QUICKSTART.md](docs/QUICKSTART.md) has copy-paste recipes for
LM Studio, Ollama, vLLM and OpenAI.

## 🛠 Manual install (macOS / Linux / purists)

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium   # downloads Chromium
python startbrowser.py
```

Or install it as a package with a `fluffbrowser` command:

```bash
pip install -e ".[dev]"
fluffbrowser            # reads .env / FLUFFBROWSER_* variables
```

## ⚙️ Configuration

Everything is documented in [docs/CONFIGURATION.md](docs/CONFIGURATION.md). The short version:

| Where | Wins over | Good for |
| --- | --- | --- |
| `FLUFFBROWSER_*` env vars | everything | CI, scripts, throwaway runs |
| `.env` file | `startbrowser.py` | keeping keys out of git |
| `startbrowser.py` CONFIG block | — | the "just edit and run" path |

| Setting | Default | Meaning |
| --- | --- | --- |
| `BASE_URL` | `http://localhost:1234/v1` | OpenAI-compatible endpoint |
| `API_KEY` | `your-api-key` | bearer token for that endpoint |
| `MODEL` | `your-model-name` | model id the server exposes |
| `TEMPERATURE` | `0.0` | 0 = deterministic |
| `MAX_STEPS` | `15` | browser actions per task |
| `TASK_TIMEOUT` | `600` | seconds per task |
| `HEADLESS` | `False` | hide the browser window |
| `BROWSER_TYPE` | `chromium` | browser-use browser kind (`chromium`/`chrome`) |

## 🗂 Project layout

```text
fluffbrowser/
├── startbrowser.py            ← ① edit the CONFIG block here
├── run.bat                    ← ② double-click to launch
├── fluffbrowser/
│   ├── app.py                 task loop, browser lifecycle
│   ├── config.py              Settings + .env / env-var overrides
│   ├── theme.py               the beige palette
│   ├── assets/logo.txt        the 3D ASCII logo
│   ├── core/
│   │   ├── agent.py           LLM wiring, one task run
│   │   └── browser.py         Chromium session helpers
│   └── ui/
│       ├── console.py         shared rich Console
│       ├── logo.py            two-tone logo renderer
│       ├── screens.py         welcome screen, panels, prompts
│       └── strings.py         every user-facing string (translate here)
├── docs/                      quickstart, configuration, architecture, troubleshooting
├── examples/                  sample tasks to try
├── tests/                     stdlib unit tests for the config layer
├── .github/                   CI, Dependabot, issue/PR templates
├── .env.example               copy to .env to keep keys out of git
├── requirements.txt
├── run.bat                    bootstrap: venv → deps → Chromium → app
└── pyproject.toml
```

More detail: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) · docs index:
[docs/README.md](docs/README.md).

## 🔄 How a task flows

```text
your text ──► build_llm() ──► Agent(browser-use)
                                 │
                                 ├─ reads the page (DOM, no screenshots)
                                 ├─ picks an action: click / type / scroll / go
                                 └─ repeats until done or MAX_STEPS
                                 │
                                 ▼
                       final answer ──► Markdown panel in your terminal
```

## 🩺 Something broke?

[docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) covers the classics: `run.bat` cannot find
Python, Chromium cannot download, `404` on `BASE_URL`, models that never call tools.

## 🔐 Privacy

- FluffBrowser has no accounts, no servers and no analytics of its own.
- Your prompt and page content go only to the endpoint in `BASE_URL`.
- Keys live in `startbrowser.py` (placeholder only in git), `.env` (git-ignored) or your shell.
- `browser-use` sends anonymised usage stats by default; add `ANONYMIZED_TELEMETRY=false` to
  `.env` to switch that off completely.

## 🤝 Contributing

Issues and pull requests are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).
Security notes live in [SECURITY.md](SECURITY.md); publishing your fork is described in
[docs/PUBLISHING.md](docs/PUBLISHING.md).

## 📄 License

[MIT](LICENSE) © FluffBrowser contributors.

## ⚠️ A friendly warning

The agent operates a real browser with your machine's privileges. Keep an eye on long tasks and
never point it at accounts you would not let a stranger click around in.

<div align="center"><sub>Made with cream, bronze and a little bit of fluff.</sub></div>
