"""A single shared :class:`rich.console.Console` instance."""

from __future__ import annotations

import sys
from typing import Any

from rich.console import Console


def _tolerate_legacy_codepages() -> None:
    """Let the logo survive cp866/cp1251 consoles and redirected output.

    Interactive Windows consoles are written through the Unicode console API,
    so this mainly protects piped runs and very old terminals. Failures are
    ignored: rendering matters, encoding never should crash the app.
    """
    for stream_name in ("stdout", "stderr"):
        stream: Any = getattr(sys, stream_name, None)
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        try:
            reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, OSError, ValueError):
            continue


_tolerate_legacy_codepages()

#: One console for the whole app so styles, width and recording stay consistent.
console = Console()

__all__ = ["console"]
