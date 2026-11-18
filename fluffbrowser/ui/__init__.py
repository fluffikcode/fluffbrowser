"""Terminal presentation layer: logo, palette-driven screens and prompts."""

from .console import console
from .logo import render_logo

__all__ = ["console", "render_logo"]
