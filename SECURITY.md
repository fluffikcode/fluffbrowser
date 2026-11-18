# Security policy

## Never commit credentials

FluffBrowser is designed so a key never has to enter the repository:

- `API_KEY` in `startbrowser.py` ships as the placeholder `your-api-key`;
- `.env` is git-ignored, `.env.example` holds placeholders only;
- environment variables (`FLUFFBROWSER_*`) override everything and leave no file behind;
- `config.masked_api_key()` exists for diagnostics that need to show a key (`••••••abcd`).

Before pushing, sanity-check what git will publish:

```bash
git status
git diff --cached
git grep -nE "sk-|api[_-]?key|trycloudflare|bearer"
```

If a key leaks: revoke it at the provider first, then rewrite history
(`git filter-repo` / BFG) and force-push. Deleting the file in a new commit is **not** enough.

## Scope of the agent

The agent drives a real Chromium session with the privileges of your user account. It can
click, type, download and navigate wherever the site allows. Treat every task as if a very
literal assistant were using your computer:

- do not point it at banking, admin or production dashboards unattended;
- watch long autonomous runs;
- prefer a throwaway browser profile for experiments;
- review what the model is being asked to do before running untrusted task text.

## Privacy

FluffBrowser itself never phones home. It does not run a server, does not store history and has
no accounts.

Third-party `browser-use` sends anonymised usage statistics to PostHog by default. To disable it:

```dotenv
# .env
ANONYMIZED_TELEMETRY=false
```

Or, for one session: `$env:ANONYMIZED_TELEMETRY="false"` (PowerShell) /
`ANONYMIZED_TELEMETRY=false python startbrowser.py`.

## Reporting a vulnerability

Please do not open a public issue for a security problem. Contact the maintainers privately
(for example via the GitHub *Security → Report a vulnerability* form) and include:

- affected version / commit,
- a minimal reproduction,
- impact you believe it has.

You can expect an acknowledgement within a few days. Please allow time for a fix before
disclosing publicly.

## Supported versions

The latest released minor version receives security fixes.
