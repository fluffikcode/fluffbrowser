"""FluffBrowser core: the LLM agent and the browser session it drives."""

from .agent import build_llm, run_task
from .browser import close_browser, create_browser

__all__ = ["build_llm", "close_browser", "create_browser", "run_task"]
