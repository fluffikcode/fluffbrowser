# Troubleshooting

## `run.bat` closes instantly / "python is not recognized"

- Install **Python 3.11+** from [python.org](https://www.python.org/downloads/) and tick
  *"Add python.exe to PATH"* during setup.
- Verify in a fresh terminal: `py -3 --version` or `python --version`.
- The launcher tries `py -3`, then `python`, then the usual install folders
  (`%LOCALAPPDATA%\Programs\Python\Python313|312|311`, `%ProgramFiles%\Python3*`), so a Python
  that is installed but missing from PATH still works.

## "Could not create a virtual environment"

- Some antivirus tools block `python -m venv`. Create it manually:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium
```

## `pip install` fails

- Behind a proxy? `pip install --proxy http://user:pass@host:port -r requirements.txt`.
- Corporate TLS interception? `pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt`.
- `browser-use` needs a recent pip: the launcher upgrades pip first when it builds the venv.
  Run `run.bat --update` to upgrade dependencies inside an existing venv.

## Chromium does not download

```powershell
.\.venv\Scripts\python.exe -m playwright install chromium
```

- Diagnose the whole stack at once: `browser-use --doctor`.
- `browser-use install` is the upstream equivalent; it shells out to `uvx`, so it needs
  [uv](https://docs.astral.sh/uv/) installed. With uv present it works just as well.
- Already have Google Chrome? Set `BROWSER_TYPE = "chrome"` in `startbrowser.py` and skip the
  download — `browser-use` drives your installed Chrome.
- Corporate proxy blocking the CDN? Set `HTTPS_PROXY` before the command, or pre-seed the
  Playwright browser cache (`%LOCALAPPDATA%\ms-playwright` on Windows,
  `~/.cache/ms-playwright` elsewhere) from a machine that already has it.
- On Linux, missing system libraries cause a silent failure — install the usual suspects
  (`libnss3`, `libatk-bridge2.0-0`, `libgtk-3-0`, `libasound2`).

## `404`, `401` or `Connection refused` when a task starts

| Symptom | Fix |
| --- | --- |
| `Connection refused` | The local server is not running, or the port is wrong |
| `404 Not Found` | `BASE_URL` is missing the `/v1` suffix (or has it twice) |
| `401 Unauthorized` | `API_KEY` is wrong or empty for a hosted provider |
| `model not found` | `MODEL` must match the id your server lists exactly |

Quick check without FluffBrowser:

```bash
curl http://localhost:1234/v1/models
```

## The agent keeps looping, or answers without doing anything

- The model probably cannot **call tools**. Pick an Instruct/tool-calling model
  (Qwen2.5 Instruct, Llama 3.1 Instruct, Mistral Nemo, GPT-4o-mini…).
- Raise `MAX_STEPS` for multi-page research.
- Lower `TEMPERATURE` to `0.0` for predictable clicking.
- Very small models (< 7B) struggle with multi-step browsing — try 7B+.

## "Задача завершена (текстовый результат отсутствует)"

The task ran but the agent produced no final text — usually it hit `MAX_STEPS` or the page was
unreachable. Ask a more specific question, or increase `MAX_STEPS`.

## The answer panel is empty or garbled

- Windows terminal too narrow? Widen it — the layout is capped at 100 columns.
- Old console? Use Windows Terminal; `rich` needs a UTF-8 capable font (Cascadia, Consolas).
- Mojibake when piping output? Set `PYTHONIOENCODING=utf-8`.

## Keyboard shortcuts

| Key | Effect |
| --- | --- |
| `Ctrl+C` | Abort the current task, close the browser, exit |
| `Ctrl+Z` then `Enter` | End of input (treated like `exit`) |

## Still stuck?

Open an issue with: OS, Python version, `pip show browser-use` output, the exact error panel
text, and **never** your API key. See [../SECURITY.md](../SECURITY.md).
