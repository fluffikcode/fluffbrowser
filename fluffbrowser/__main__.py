"""Allow ``python -m fluffbrowser``.

Settings come from ``.env`` / ``FLUFFBROWSER_*`` variables; use
``startbrowser.py`` if you prefer editing the config block directly.
"""

from .app import main

if __name__ == "__main__":
    main()
