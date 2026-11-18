"""The 3D ASCII logo and its two-tone rendering."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from rich.text import Text

from ..theme import BRONZE, CREAM

#: Packaged so an installed copy keeps its logo.
LOGO_PATH = Path(__file__).resolve().parent.parent / "assets" / "logo.txt"

#: Box-drawing characters that act as the "shadow" of the 3D lettering.
SHADOW_CHARS = frozenset("╔═╗║╚╝╦╩╠╣╬")


@lru_cache(maxsize=1)
def raw_logo() -> str:
    """Load the logo once; fall back to a plain wordmark if the asset is missing."""
    try:
        return LOGO_PATH.read_text(encoding="utf-8").rstrip("\n")
    except OSError:
        return "F L U F F B R O W S E R"


def render_logo() -> Text:
    """Two-tone effect: light cream faces, dark bronze shadows."""
    logo = Text()
    for char in raw_logo():
        if char == "█":
            logo.append(char, style=f"bold {CREAM}")
        elif char in SHADOW_CHARS:
            logo.append(char, style=BRONZE)
        else:
            logo.append(char)
    return logo


__all__ = ["SHADOW_CHARS", "raw_logo", "render_logo"]
