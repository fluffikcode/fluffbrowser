#!/usr/bin/env python3
"""FluffBrowser — start here.

    ╔══════════════════════════════════════════════════════════════╗
    ║  ①  Edit the CONFIG block below (BASE_URL, API_KEY, MODEL)   ║
    ║  ②  Double-click run.bat  (or: python startbrowser.py)       ║
    ╚══════════════════════════════════════════════════════════════╝

Everything else lives in the ``fluffbrowser/`` package:

    fluffbrowser/app.py         task loop and shutdown
    fluffbrowser/config.py      settings, .env and FLUFFBROWSER_* variables
    fluffbrowser/core/agent.py  LLM wiring and agent runs
    fluffbrowser/core/browser.py  Chromium lifecycle
    fluffbrowser/ui/            logo, palette, screens, strings
"""

from __future__ import annotations

import asyncio

from fluffbrowser.app import run
from fluffbrowser.config import Settings

# ══════════════════════════════════════════════════════════════════════════
#  ①  CONFIG — any OpenAI-compatible endpoint works
# ══════════════════════════════════════════════════════════════════════════
BASE_URL = "http://localhost:1234/v1"  # LM Studio default; OpenAI: https://api.openai.com/v1
API_KEY = "your-api-key"  # LM Studio/Ollama ignore it, hosted APIs require the real key
MODEL = "your-model-name"  # e.g. "qwen2.5-7b-instruct", "gpt-4o-mini"

TEMPERATURE = 0.0  # 0.0 = deterministic, higher = more creative
MAX_STEPS = 15  # how many browser actions the agent may take per task
TASK_TIMEOUT = 600  # seconds before a single task is aborted
HEADLESS = False  # keep the browser window visible
BROWSER_TYPE = "chromium"  # or "chrome"
# ══════════════════════════════════════════════════════════════════════════


def load_settings() -> Settings:
    """Config block above, optionally overridden by .env / FLUFFBROWSER_* vars."""
    return Settings(
        base_url=BASE_URL,
        api_key=API_KEY,
        model=MODEL,
        temperature=TEMPERATURE,
        max_steps=MAX_STEPS,
        timeout=TASK_TIMEOUT,
        headless=HEADLESS,
        browser_type=BROWSER_TYPE,
    ).with_env_overrides()


if __name__ == "__main__":
    try:
        asyncio.run(run(load_settings()))
    except KeyboardInterrupt:
        pass
