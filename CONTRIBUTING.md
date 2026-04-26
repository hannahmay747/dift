# Contributing to Dift

Thanks for your interest in contributing to Dift.

## Ways to Contribute

- Report bugs
- Suggest features
- Improve docs
- Add tests
- Improve performance
- Add connectors and integrations

## Development Setup

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Lint:

```bash
ruff check .
```

## Branching

Create a feature branch:

```bash
git checkout -b feature/my-change
```

## Commit Style

Use clear commit messages:

```text
feat: add parquet schema diff
fix: handle null numeric columns
Docs: improve installation steps
```

## Pull Requests

Please include:

- What changed
- Why it changed
- Screenshots/output if relevant
- Tests added or updated

## Code Guidelines

- Keep functions small and readable
- Add type hints where practical
- Add tests for new behavior
- Prefer performance-conscious implementations
- Preserve backward compatibility when possible

## Good First Issues

- Improve CLI UX
n- Add HTML report template
- Add more fixtures in examples/
- Improve error messages
- Add benchmarks

## Community

Be respectful, constructive, and helpful.

We welcome contributors of all skill levels.

