"""Browser session lifecycle.

``browser-use`` changed its constructor between 0.x and 1.x:

- **1.x** — ``Browser("chromium", headless=False)`` (positional kind)
- **0.4/0.5** — ``Browser(config=BrowserConfig(headless=False))``

The signature is inspected once, so either generation works and a future
upgrade only needs a new branch here.
"""

from __future__ import annotations

import contextlib
import inspect

from browser_use import Browser

from ..config import Settings


def _browser_options(settings: Settings) -> dict[str, object]:
    return {"headless": settings.headless, "browser_type": settings.browser_type}


def _from_browser_config(settings: Settings) -> Browser | None:
    """0.4–0.5 style constructor; ``BrowserConfig`` no longer exists in 1.x."""
    try:
        from browser_use import BrowserConfig  # type: ignore[attr-defined]
    except ImportError:
        return None

    for options in (_browser_options(settings), {"headless": settings.headless}):
        try:
            return Browser(config=BrowserConfig(**options))
        except (TypeError, ValueError):
            continue
    return None


def create_browser(settings: Settings) -> Browser:
    """Create (but do not start) the browser session."""
    parameters = inspect.signature(Browser.__init__).parameters

    if "config" in parameters and "kind" not in parameters:
        browser = _from_browser_config(settings)
        if browser is not None:
            return browser

    last_error: Exception | None = None
    for attempt in (
        lambda: Browser(settings.browser_type, headless=settings.headless),
        lambda: Browser(headless=settings.headless),
    ):
        try:
            return attempt()
        except (TypeError, ValueError) as exc:
            last_error = exc

    raise RuntimeError(
        "Не удалось создать сессию браузера: неподдерживаемая версия browser-use. "
        "Обновите пакет командой: pip install -U browser-use"
    ) from last_error


async def close_browser(browser: Browser | None) -> None:
    """Close the session, ignoring "already closed" style errors."""
    if browser is None:
        return
    with contextlib.suppress(Exception):
        await browser.close()


__all__ = ["close_browser", "create_browser"]
