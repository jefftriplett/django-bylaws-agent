# Django Bylaws Agent - Development Guide

## Commands
- `just` - List all available commands
- `just bootstrap` - Install pip and uv (Python package management)
- `just demo` - Run a demo with a sample question
- `just fmt` - Format code using ruff
- `just lint` - Run linting on all files
- `just pre-commit` - Run pre-commit hooks

## Code Style Guidelines
- **Python version**: Target Python 3.12+
- **Line length**: 120 characters maximum
- **Linting**: Use ruff with E (pycodestyle) and F (pyflakes) rules
- **Formatting**: Follow PEP 8 conventions with ruff 
- **Imports**: Sort imports with ruff
- **Type hints**: Use static typing throughout codebase
- **Naming**: Use snake_case for variables/functions, PascalCase for classes
- **Error handling**: Use explicit try/except blocks with specific exception types
- **Dependencies**: httpx, environs, pydantic-ai-slim[openai], rich, typer

## Project Structure
This tool uses OpenAI APIs to answer questions about Django Software Foundation bylaws.