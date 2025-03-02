# Django Bylaws Agent (Unofficial)

An AI Agent that helps answer common questions about Django Software Foundation's Bylaws.

Please note: This is not official or legal advice.

## Usage

You can use either the `just ask` command or run the agent directly:

```shell
$ just ask "How long are director terms?"
# or
$ uv run agent.py "How long are director terms?"

Answer: Director terms are for two (2) years.

Reasoning: According to Section 4.4.1 of the Django Software Foundation's Bylaws, directors are elected to two-year terms. This means that once elected, each director
holds office for a period of two years until their successor is elected or until other circumstances such as resignation or removal occur.

Sections:
- Section 4.4.1
```

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
