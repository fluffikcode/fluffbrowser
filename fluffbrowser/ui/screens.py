"""Screens, panels and prompts of the FluffBrowser interface.

Nothing here knows about LLMs or browsers — it only renders and reads input,
which keeps the visual language easy to tweak.
"""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from contextlib import contextmanager

from rich import box
from rich.align import Align
from rich.markdown import Markdown
from rich.panel import Panel

from .. import __version__
from ..theme import BEIGE, BRONZE, CREAM, MUTED, SAGE, TERRA
from . import strings
from .console import console
from .logo import render_logo


@contextmanager
def status(message: str, *, spinner: str = "dots", style: str = MUTED) -> Iterator[None]:
    """Calm, single-line loader used instead of raw print statements."""
    with console.status(message, spinner=spinner, spinner_style=style):
        yield


def show_welcome_screen() -> None:
    """Full start screen: logo, greeting card and command hints."""
    console.clear()
    console.print()

    console.print(Align.center(render_logo()))

    welcome_info = (
        f"[bold {CREAM}]{strings.TAGLINE}[/bold {CREAM}]\n"
        f"[{MUTED}]{strings.DESCRIPTION}[/{MUTED}]\n\n"
        f"[{BEIGE}]{strings.COMMANDS_LABEL}[/{BEIGE}]  "
        f"[bold {CREAM}]{strings.CMD_CLEAR}[/bold {CREAM}] "
        f"[{MUTED}]{strings.CMD_CLEAR_HINT}[/{MUTED}]   •   "
        f"[bold {CREAM}]{strings.CMD_EXIT}[/bold {CREAM}] "
        f"[{MUTED}]{strings.CMD_EXIT_HINT}[/{MUTED}]"
    )

    panel = Panel(
        Align.center(welcome_info),
        title=f"[{BEIGE}]{strings.WELCOME_TITLE}[/{BEIGE}]",
        subtitle=f"[{MUTED}]{strings.SUBTITLE_TEMPLATE.format(version=__version__)}[/{MUTED}]",
        border_style=BRONZE,
        box=box.ROUNDED,
        padding=(1, 4),
    )
    console.print(Align.center(panel, width=100))
    console.print()


def show_setup_warnings(messages: Sequence[str]) -> None:
    """Gentle reminder that the config block still needs a real endpoint/key."""
    if not messages:
        return

    body = "\n".join(f"[{CREAM}]• {message}[/{CREAM}]" for message in messages)
    body += f"\n\n[{MUTED}]{strings.CONFIG_HINT}[/{MUTED}]"

    console.print(
        Panel(
            body,
            title=f"[bold {TERRA}]{strings.CONFIG_TITLE}[/bold {TERRA}]",
            title_align="left",
            border_style=TERRA,
            box=box.ROUNDED,
            padding=(0, 2),
        )
    )
    console.print()


def show_ready() -> None:
    """Announce that the browser session is up."""
    console.print(f"[{SAGE}]{strings.READY}[/{SAGE}]\n")


def show_browser_closed() -> None:
    """Final line after a clean shutdown."""
    console.print(f"[{MUTED}]{strings.CLOSED}[/{MUTED}]")


def read_command() -> str:
    """Minimalist two-line input prompt."""
    console.print(f"╭─ [{BEIGE}]{strings.PROMPT_TITLE}[/{BEIGE}]")
    return console.input(f"╰─[{BRONZE}]{strings.PROMPT_ARROW}[/{BRONZE}] ")


def show_result(answer: str) -> None:
    """Render the agent's Markdown answer inside a sage frame."""
    console.print()
    console.print(
        Panel(
            Markdown(answer),
            title=f"[bold {SAGE}]{strings.RESULT_TITLE}[/bold {SAGE}]",
            title_align="left",
            border_style=SAGE,
            box=box.ROUNDED,
            padding=(1, 2),
        )
    )


def show_error(message: str) -> None:
    """Render an exception message inside a terracotta frame."""
    console.print()
    console.print(
        Panel(
            f"[{CREAM}]{message}[/{CREAM}]",
            title=f"[bold {TERRA}]{strings.ERROR_TITLE}[/bold {TERRA}]",
            title_align="left",
            border_style=TERRA,
            box=box.ROUNDED,
            padding=(0, 2),
        )
    )


def show_goodbye() -> None:
    """Small closing panel when the user types ``exit``."""
    console.print()
    console.print(
        Panel(
            f"[{BEIGE}]{strings.GOODBYE}[/{BEIGE}]",
            border_style=BRONZE,
            box=box.ROUNDED,
            expand=False,
            padding=(0, 3),
        )
    )


def show_interrupt() -> None:
    """Shown on Ctrl+C."""
    console.print(f"\n[{TERRA}]{strings.INTERRUPT}[/{TERRA}]")


def show_divider() -> None:
    """Thin separator between tasks."""
    console.print(f"[{MUTED}]  {'─' * 60}[/{MUTED}]")


__all__ = [
    "read_command",
    "show_browser_closed",
    "show_divider",
    "show_error",
    "show_goodbye",
    "show_interrupt",
    "show_ready",
    "show_result",
    "show_setup_warnings",
    "show_welcome_screen",
    "status",
]
