# Architecture

FluffBrowser is deliberately small: one entry point, one package, no state beyond the browser
session. Reading a handful of files in order is enough to understand the whole app.

## Layers

```text
startbrowser.py        the editable config block + asyncio.run(run(settings))
        │
        ▼
fluffbrowser/app.py    welcome screen → task loop → shutdown
        │
        ├── config.py          Settings, .env loader, env-var overrides, validation
        ├── theme.py           the six-colour palette
        ├── assets/logo.txt    the 3D ASCII logo
        │
        ├── core/browser.py    create / close the Chromium session
        ├── core/agent.py      build the LLM client, run one agent task
        │
        └── ui/
            ├── console.py     one shared rich Console
            ├── logo.py        loads assets/logo.txt, renders the two-tone logo
            ├── screens.py     panels, prompts, status spinners
            └── strings.py     all user-facing text
```

Dependency direction is strictly one-way: `ui` never imports `core`, `core` never imports
`app`. That keeps the interface reusable and the agent testable.

## Startup sequence

1. `startbrowser.py` builds `Settings` from its CONFIG block.
2. `Settings.with_env_overrides()` loads `.env` and applies `FLUFFBROWSER_*` variables.
3. `app.run()` paints the welcome screen and, if the key is still a placeholder or the URL is
   not HTTP, shows a non-blocking warning panel.
4. `build_llm()` creates a `ChatOpenAI` client — the only place a provider is configured.
5. `create_browser()` constructs (does not start) a Chromium session; `browser-use` launches
   the process lazily on the first task.
6. The REPL reads a command, recognises `clear` / `exit`, otherwise hands the text to
   `run_task()`.

## One task

```text
Agent(task=..., llm=..., browser=..., use_vision=False)
    └─ agent.run(max_steps=MAX_STEPS, timeout=TASK_TIMEOUT)
            └─ loop: observe DOM → ask the model → execute an action
    └─ result.final_result()  → Markdown panel, or an error panel on exception
```

Design choices worth knowing:

- **Vision is off.** The agent reasons over the DOM instead of screenshots, which is cheaper
  and works with text-only models.
- **The browser outlives tasks.** One session, many tasks — cookies and logins persist until
  you exit.
- **Errors are UI.** Any exception inside a task becomes a terracotta panel; the session keeps
  running. Only a failed browser start ends the program.
- **Shutdown is unconditional.** `finally:` closes the browser and prints the last line, also
  after `Ctrl+C` or EOF.

## Extending FluffBrowser

| Want to… | Touch |
| --- | --- |
| Change colours | `theme.py` |
| Change wording / translate the UI | `ui/strings.py` |
| Change layout of a panel | `ui/screens.py` |
| Try a different agent library | `core/agent.py` |
| Add browser flags (proxy, profile, window size) | `core/browser.py` |
| Add settings | `config.py` + `startbrowser.py` + `docs/CONFIGURATION.md` |

## Compatibility notes

`browser-use` evolves quickly. Version 1.x takes `Browser("chromium", headless=False)`, while
0.4/0.5 expected a `BrowserConfig` object. `core/browser.py` inspects the constructor signature
and adapts to either, raising a single readable error if neither matches. If a future release
breaks the app, that file is the first place to look.
