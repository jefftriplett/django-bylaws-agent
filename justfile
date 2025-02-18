set dotenv-load := false

export JUST_UNSTABLE := "true"

@_default:
    just --list

@bootstrap *ARGS:
    pip install --upgrade pip uv

@demo:
    uv --quiet run django-bylaws-agent.py "How long are director's terms?"

@fmt:
    just --fmt

@lint *ARGS:
    just pre-commit {{ ARGS }} --all-files

@pre-commit *ARGS:
    uv --quiet tool run --with pre-commit-uv pre-commit run {{ ARGS }}
