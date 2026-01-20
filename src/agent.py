#!/usr/bin/env -S uv --quiet run
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "httpx",
#     "environs",
#     "pydantic-ai-slim[openai]",
#     "rich",
#     "typer",
# ]
# ///

import httpx
import typer

from environs import env
from pathlib import Path
from pydantic import BaseModel
from pydantic import Field
from pydantic_ai import Agent
from rich.console import Console

console = Console()

OPENAI_API_KEY: str = env.str("OPENAI_API_KEY")
OPENAI_MODEL_NAME: str = env.str("OPENAI_MODEL_NAME", default="gpt-5-mini")

SYSTEM_PROMPT = """
<system_context>

You are a bylaws policy assistant for the Django Software Foundation.

</system_context>

<behavior_guidelines>

- Please answer all questions using Django's bylaws.
- Please warn the user that this not official or legal advice.

</behavior_guidelines>
"""


class Output(BaseModel):
    answer: str = Field(description="The answer to our question")
    reasoning: str = Field(description="The reasoning and support for our answer based on our source material")
    sections: list[str] = Field(description="Sections to reference")


def fetch_and_cache(
    *,
    url: str,
    cache_file: str,
    timeout: float = 10.0,
):
    filename = Path(cache_file)
    if filename.exists():
        return filename.read_text()

    response = httpx.get(f"https://r.jina.ai/{url}", timeout=timeout)
    response.raise_for_status()

    contents = response.text

    Path(cache_file).write_text(contents)

    return contents


def get_django_bylaws_agent():
    bylaws = fetch_and_cache(
        url="https://media.djangoproject.com/foundation/bylaws.pdf",
        cache_file="django-bylaws.md",
    )

    agent = Agent(
        model=OPENAI_MODEL_NAME,
        output_type=Output,
        system_prompt=SYSTEM_PROMPT,
    )

    @agent.instructions
    def add_bylaws() -> str:
        return f"<bylaws>\n\n{bylaws}\n\n</bylaws>"

    return agent


app = typer.Typer(help="Django Bylaws Agent - Ask questions about DSF bylaws")


@app.command()
def ask(question: str, model_name: str = OPENAI_MODEL_NAME):
    """Ask the bylaws agent a question."""
    agent = get_django_bylaws_agent()

    result = agent.run_sync(question)

    console.print(
        f"[green][bold]Answer:[/bold][/green] {result.output.answer}\n\n"
        f"[yellow][bold]Reasoning:[/bold][/yellow] {result.output.reasoning}\n"
    )

    if result.output.sections:
        console.print("[yellow][bold]Sections:[/bold][/yellow]")
        for section in result.output.sections:
            console.print(f"- {section}")


@app.command()
def debug():
    """Print the compiled system prompt for debugging."""
    bylaws = fetch_and_cache(
        url="https://media.djangoproject.com/foundation/bylaws.pdf",
        cache_file="django-bylaws.md",
    )

    console.print("[bold cyan]===== SYSTEM PROMPT =====[/bold cyan]\n")
    console.print(SYSTEM_PROMPT)
    console.print("\n[bold cyan]===== INSTRUCTIONS =====[/bold cyan]\n")
    console.print(f"<bylaws>\n\n{bylaws}\n\n</bylaws>")
    console.print("\n[bold cyan]=========================[/bold cyan]")


if __name__ == "__main__":
    app()
