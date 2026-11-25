# Django Bylaws Agent (Unofficial)

An AI Agent that helps answer common questions about Django Software Foundation's Bylaws.

Please note: This is not official or legal advice.

## Usage

You can use either the `just ask` command or run the agent directly:

```shell
$ just ask "How long are director terms?"
# or
$ uv run src/agent.py "How long are director terms?"

Answer: Director terms are for two (2) years.

Reasoning: According to Section 4.4.1 of the Django Software Foundation's Bylaws, directors are elected to two-year terms. This means that once elected, each director
holds office for a period of two years until their successor is elected or until other circumstances such as resignation or removal occur.

Sections:
- Section 4.4.1
```

## Environment Variables

- `PYDANTIC_AI_MODEL`: Model to use (default: `openai:gpt-5.4-nano`)
- The API key for that model's provider, e.g. `OPENAI_API_KEY` for the default (see the table below)

`PYDANTIC_AI_MODEL` is a [Pydantic AI model reference](https://ai.pydantic.dev/models/) in
`provider:model` form. The prefix is required — a bare model name raises `Unknown model` —
and it is what selects the provider:

| Prefix | API key | Notes |
|--------|---------|-------|
| `openai:` | `OPENAI_API_KEY` | The default (`openai:gpt-5.4-nano`) |
| `deepseek:` | `DEEPSEEK_API_KEY` | Works as-is |
| `openrouter:` | `OPENROUTER_API_KEY` | Works as-is |
| `together:` | `TOGETHER_API_KEY` | Works as-is |
| `ollama:` | `OLLAMA_API_KEY` | Works as-is; set `OLLAMA_BASE_URL` for a local server |
| `anthropic:` | `ANTHROPIC_API_KEY` | Needs the `anthropic` extra |
| `google:` | `GEMINI_API_KEY` or `GOOGLE_API_KEY` | Needs the `google` extra |
| `groq:` | `GROQ_API_KEY` | Needs the `groq` extra |
| `mistral:` | `MISTRAL_API_KEY` | Needs the `mistral` extra |
| `cohere:` | `CO_API_KEY` | Needs the `cohere` extra |
| `xai:` | `XAI_API_KEY` | Needs the `xai` extra |
| `bedrock:` | AWS credentials | Needs the `bedrock` extra |

```shell
export PYDANTIC_AI_MODEL=openai:gpt-5.4
export PYDANTIC_AI_MODEL=deepseek:deepseek-chat
```

"Works as-is" means the provider runs on the OpenAI SDK this agent already installs, so
only its API key is needed. The rest need their extra added to `pydantic-ai-slim[...]` in
the script header of `src/agent.py`. Only the chosen provider's key is needed; `just doctor`
checks that it is set. `ask --model-name` overrides the model for a single question.

## Installation

```shell
$ just bootstrap  # Install required tools
```

## Development

```shell
$ just           # List all available commands
$ just demo      # Run a demo with a sample question
$ just fmt       # Format code using ruff
$ just lint      # Run linting on all files
```
