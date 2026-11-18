# Example tasks

Copy any line into FluffBrowser and press Enter. Keep them specific — the agent clicks what you
describe, so "find X on Y" beats "browse the internet".

## Browsing basics

```text
open example.com and tell me what this site is about
open wikipedia.org, search for "capybara" and summarise the first two paragraphs
go to news.ycombinator.com and list the five top stories with their point counts
open github.com/trending and tell me which Python project is number one today
```

## Research

```text
find the current EUR to USD exchange rate on xe.com and convert 250 EUR
open the weather page for Berlin and tell me the forecast for tomorrow
search for "browser-use" on PyPI and tell me the latest version and its release date
```

## Practical chores

```text
open the site of my local library, search for "Dune" and tell me whether it is available
open a currency converter and calculate 199 USD in JPY
open the docs of the "rich" Python library and find how to print a panel with a title
```

## Testing the agent itself

```text
open example.com, scroll to the bottom, then tell me the last sentence on the page
open a blank tab, search for "fluffbrowser" on GitHub and report how many repositories exist
```

## Tips

- One goal per task. Split complex plans into a few messages.
- Ask for the *answer*, not for a description of the clicks.
- If the agent loops, rephrase with the exact site name and a concrete target.
- `MAX_STEPS` (default 15) is the budget per task — raise it for multi-page research.
