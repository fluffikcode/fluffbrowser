"""The LLM configuration and a single agent task run."""

from __future__ import annotations

from browser_use import Agent, Browser, ChatOpenAI

from ..config import Settings
from ..theme import BRONZE
from ..ui import screens, strings
from ..ui.console import console


def build_llm(settings: Settings) -> ChatOpenAI:
    """Any OpenAI-compatible endpoint works: LM Studio, Ollama, vLLM, OpenAI..."""
    return ChatOpenAI(
        model=settings.model,
        base_url=settings.base_url,
        api_key=settings.api_key,
        temperature=settings.temperature,
    )


async def run_task(
    command: str,
    *,
    browser: Browser,
    llm: ChatOpenAI,
    settings: Settings,
) -> None:
    """Hand one free-form task to the agent and print the answer."""
    console.print()
    try:
        agent = Agent(
            task=command,
            llm=llm,
            browser=browser,
            use_vision=False,
        )

        with screens.status(strings.BUSY_TASK, spinner="aesthetic", style=BRONZE):
            result = await agent.run(max_steps=settings.max_steps, timeout=settings.timeout)

        answer = result.final_result() or strings.RESULT_FALLBACK
        screens.show_result(answer)

    except Exception as exc:  # shown as a themed panel instead of a traceback
        screens.show_error(str(exc))


__all__ = ["build_llm", "run_task"]
