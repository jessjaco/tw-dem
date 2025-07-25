# Python Template

A Python package template with [uv](https://docs.astral.sh/uv/), [pre-commit hooks](https://pre-commit.com), and GitHub Actions for CI/CD.

## Features

- 📦 [**uv**](https://docs.astral.sh/uv/) for dependency management and packaging
- 🔧 [**Pre-commit hooks**](https://pre-commit.com) for code quality (primarily using [Ruff](https://docs.astral.sh/ruff/))
- 🏷️ **pyright** for type checking
- 🧪 **Pytest** with coverage reporting
- 🚀 **GitHub Act ions** for automated testing and checks
- 📋 **PR template** and contributing guidelines
- 🐍 **Python 3.12+** support

## Quick Start

### Using This Template

1. **Click "Use this template"** on GitHub

2. **Install uv** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install dependencies**:
   ```bash
   uv sync --dev
   ```

4. **Set up pre-commit hooks**:
   ```bash
   uv run pre-commit install
   ```

5. **Customize for your project**:
   - Update `pyproject.toml` with your project details
   - Rename the `python_template` directory to your package name along with any other references to this directory
   - Update this README with your project information

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

### Project Structure
```
python-template/
├── python_template/          # Main package (rename this)
├── tests/                    # Test directory
├── .github/                  # GitHub templates and workflows
├── .pre-commit-config.yaml   # Pre-commit configuration
├── pyproject.toml           # Project configuration
└── README.md
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development workflow and guidelines.
