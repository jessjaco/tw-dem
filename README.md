# tw-dem

A python package to create TealWaters DEM derivatives.

## Installation

1. **Install uv** (if not already installed):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install dependencies**:

   ```bash
   uv sync --dev
   ```

3. **Set up pre-commit hooks**:

   ```bash
   uv run pre-commit install
   ```

## Development

### Running Tests

```bash
uv run pytest
```

### Code Quality

```bash
uv run pyright                  # Type check
uv run pre-commit run --all-files  # Run all hooks
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development workflow and guidelines.
