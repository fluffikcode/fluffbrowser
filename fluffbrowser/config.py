"""Settings for FluffBrowser.

Priority (highest wins):

1. ``FLUFFBROWSER_*`` environment variables
2. values from a local ``.env`` file
3. the ``CONFIG`` block in ``startbrowser.py``

That means you can keep the repo clean (no keys in git) and still configure
everything from a single obvious place.
"""

from __future__ import annotations

import os
from collections.abc import Iterable
from dataclasses import dataclass, replace
from pathlib import Path

ENV_PREFIX = "FLUFFBROWSER_"

#: Keys that mean "the user has not configured anything yet".
PLACEHOLDER_API_KEYS = frozenset(
    {"", "your-api-key", "your-api-key-here", "your_api_key", "changeme", "sk-xxx"}
)

_ENV_FILES = (
    Path.cwd() / ".env",
    Path(__file__).resolve().parents[1] / ".env",
)


def load_dotenv(paths: Iterable[Path | str] | None = None) -> None:
    """Read ``KEY=VALUE`` pairs from ``.env`` without overriding real env vars.

    Kept dependency-free on purpose: FluffBrowser only needs the simple syntax
    (comments, blank lines, optional quotes around values).

    ``paths`` is chiefly for tests; by default the current directory and the
    project root are checked.
    """
    env_files = [Path(path) for path in paths] if paths is not None else list(_ENV_FILES)
    for env_file in env_files:
        if not env_file.is_file():
            continue
        for raw_line in env_file.read_text(encoding="utf-8", errors="replace").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            if key.startswith("export "):
                key = key.removeprefix("export ").strip()
            value = value.strip().strip('"').strip("'")
            if key:
                os.environ.setdefault(key, value)


def env(name: str) -> str | None:
    """Return a ``FLUFFBROWSER_``-prefixed environment variable, if set."""
    return os.getenv(f"{ENV_PREFIX}{name}")


def _as_bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


@dataclass(frozen=True, slots=True)
class Settings:
    """Everything the app needs to talk to an LLM and drive a browser."""

    base_url: str = "http://localhost:1234/v1"
    api_key: str = "your-api-key"
    model: str = "your-model-name"
    temperature: float = 0.0
    max_steps: int = 15
    timeout: int = 600
    headless: bool = False
    browser_type: str = "chromium"

    def with_env_overrides(self) -> Settings:
        """Return a copy of these settings with ``.env`` / env vars applied."""
        load_dotenv()
        updates: dict[str, object] = {}

        for name, field in (("BASE_URL", "base_url"), ("API_KEY", "api_key"), ("MODEL", "model")):
            value = env(name)
            if value:
                updates[field] = value.strip()

        raw_temperature = env("TEMPERATURE")
        if raw_temperature:
            try:
                updates["temperature"] = float(raw_temperature)
            except ValueError:
                pass

        for name, field in (("MAX_STEPS", "max_steps"), ("TIMEOUT", "timeout")):
            raw_value = env(name)
            if raw_value:
                try:
                    updates[field] = max(1, int(raw_value))
                except ValueError:
                    pass

        raw_headless = env("HEADLESS")
        if raw_headless:
            updates["headless"] = _as_bool(raw_headless)

        raw_browser_type = env("BROWSER_TYPE")
        if raw_browser_type:
            updates["browser_type"] = raw_browser_type.strip()

        return replace(self, **updates) if updates else self

    def has_placeholder_credentials(self) -> bool:
        """True when the API key is still an example value."""
        return self.api_key.strip().lower() in PLACEHOLDER_API_KEYS

    def base_url_is_valid(self) -> bool:
        """True when ``base_url`` looks like an HTTP endpoint."""
        return self.base_url.strip().lower().startswith(("http://", "https://"))

    def masked_api_key(self) -> str:
        """Never print a real key — only its last four characters."""
        key = self.api_key.strip()
        if len(key) <= 8:
            return "•" * len(key)
        return f"{'•' * 6}{key[-4:]}"


__all__ = ["ENV_PREFIX", "Settings", "env", "load_dotenv"]
