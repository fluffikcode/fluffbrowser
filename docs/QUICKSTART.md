# Quick start

FluffBrowser talks to any **OpenAI-compatible** endpoint. Pick one recipe, paste it into the
CONFIG block of `startbrowser.py`, then launch `run.bat`.

## 1. Pick an endpoint

### LM Studio (easiest, fully local)

1. Install [LM Studio](https://lmstudio.ai), download a **tool-calling** model
   (Qwen2.5 Instruct, Llama 3.1 8B Instruct, Mistral Nemo…).
2. Start the local server (Developer → Start Server). Default port `1234`.
3. Copy the model identifier shown in the server tab.

```python
BASE_URL = "http://localhost:1234/v1"
API_KEY = "lm-studio"          # LM Studio ignores the key
MODEL = "qwen2.5-7b-instruct"  # ← the id from LM Studio
```

### Ollama

```bash
ollama pull qwen2.5:7b
ollama serve
```

```python
BASE_URL = "http://localhost:11434/v1"
API_KEY = "ollama"
MODEL = "qwen2.5:7b"
```

### vLLM / llama.cpp server

```bash
vllm serve Qwen/Qwen2.5-7B-Instruct --port 8000
```

```python
BASE_URL = "http://localhost:8000/v1"
API_KEY = "EMPTY"
MODEL = "Qwen/Qwen2.5-7B-Instruct"
```

### OpenAI / OpenRouter

```python
BASE_URL = "https://api.openai.com/v1"          # or https://openrouter.ai/api/v1
API_KEY = "sk-..."                              # keep this out of git → use .env
MODEL = "gpt-4o-mini"
```

## 2. Launch

```text
run.bat            (Windows, double-click)
python startbrowser.py              (any OS, venv activated)
```

First run: creates `.venv`, installs dependencies, downloads Chromium (~150 MB).
Later runs: instant.

## 3. First tasks to try

```text
open example.com and tell me what this site is about
```
```text
go to news.ycombinator.com and list the five top stories with their points
```
```text
search Wikipedia for "capybara" and summarise the first two paragraphs
```
```text
open github.com/trending and tell me which Python repo is trending today
```

## 4. Keep your key out of git

Instead of editing `startbrowser.py`:

```bash
copy .env.example .env     # Windows
cp .env.example .env       # macOS/Linux
```

```dotenv
FLUFFBROWSER_BASE_URL=https://api.openai.com/v1
FLUFFBROWSER_API_KEY=sk-...
FLUFFBROWSER_MODEL=gpt-4o-mini
```

`.env` is ignored by git, so `git status` stays clean.

## 5. Optional: install as a command

```bash
pip install -e ".[dev]"
fluffbrowser
```

The `fluffbrowser` command takes its settings from `.env` / `FLUFFBROWSER_*` variables only
(it never reads `startbrowser.py`).
