"""Application wiring: welcome screen → task loop → shutdown.

``startbrowser.py`` and ``python -m fluffbrowser`` both end up here.
"""

from __future__ import annotations

import asyncio

from .config import Settings
from .core.agent import build_llm, run_task
from .core.browser import close_browser, create_browser
from .theme import BEIGE, MUTED
from .ui import screens, strings


def setup_warnings(settings: Settings) -> list[str]:
    """Collect non-fatal configuration problems for the welcome screen."""
    warnings: list[str] = []
    if settings.has_placeholder_credentials():
        warnings.append(strings.WARNING_PLACEHOLDER_KEY)
    if not settings.base_url_is_valid():
        warnings.append(strings.WARNING_INVALID_URL)
    return warnings


async def run(settings: Settings) -> None:
    """Start the interface and keep it alive until the user leaves."""
    settings = settings.with_env_overrides()

    screens.show_welcome_screen()
    screens.show_setup_warnings(setup_warnings(settings))

    llm = build_llm(settings)

    try:
        with screens.status(strings.BUSY_BROWSER, spinner="dots", style=BEIGE):
            browser = create_browser(settings)
    except Exception as exc:
        screens.show_error(str(exc))
        return

    screens.show_ready()

    try:
        while True:
            command = screens.read_command().strip()
            if not command:
                continue

            lowered = command.lower()

            if lowered in strings.EXIT_COMMANDS:
                screens.show_goodbye()
                break

            if lowered in strings.CLEAR_COMMANDS:
                screens.show_welcome_screen()
                continue

            await run_task(command, browser=browser, llm=llm, settings=settings)
            screens.show_divider()

    except (KeyboardInterrupt, EOFError):
        screens.show_interrupt()

    finally:
        with screens.status(strings.BUSY_CLOSE, spinner="dots", style=MUTED):
            await close_browser(browser)
        screens.show_browser_closed()


def main() -> None:
    """Console-script entry point: ``fluffbrowser``."""
    try:
        asyncio.run(run(Settings()))
    except KeyboardInterrupt:
        pass


__all__ = ["main", "run", "setup_warnings"]
