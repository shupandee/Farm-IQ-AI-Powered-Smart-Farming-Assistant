# 🌾🧑‍💻 Contributing to Farm-IQ: The AI Farming Assistant

**Welcome!** We're thrilled you're interested in contributing to Farm-IQ! This project aims to bring the power of AI to smart farming, and your help is vital.

🥳 **This repository proudly participates in Hacktoberfest!** We encourage all skill levels to get involved, whether you're a Python coder, a data scientist, or a technical writer.

***

## 📚 Getting Started

Before you begin contributing, please:

1. **Read the [Setup Guide](SETUP_GUIDE.md)** - Learn how to set up the project locally
2. **Review the [API Documentation](API_DOCUMENTATION.md)** - Understand the endpoints and functionality
3. **Check the [README](README.md)** - Get familiar with the project overview

***

## 🚀 Ways to Contribute

We look for focused, high-impact contributions. Your help can fall into these key areas:

| Contribution Area | Focus | Goal |
| :--- | :--- | :--- |
| **Model Improvement** 🧠 | Core AI/ML logic, Model Architectures, Algorithms (Python, TensorFlow/PyTorch). | Increase prediction accuracy, optimize model speed, or reduce training time. |
| **Data & Datasets** 📊 | Sourcing, cleaning, or labeling farming data (e.g., crop diseases, soil types). | Expand the model's knowledge base and real-world applicability. |
| **New Features** 💡 | Implementing new features (e.g., automated irrigation, pest detection module). | Add powerful, practical tools for farmers. |
| **Code Maintenance** 🧹 | Refactoring, bug fixes, dependency updates, ensuring clean Python standards. | Keep the codebase fast, clean, and secure. |
| **Documentation** 📝 | Guides, explanations, API docs, usage examples. | Make the project easy for both developers and users (farmers) to understand. |

***

## 💡 Quick Start Checklist

To ensure your contribution is merged smoothly, please follow these steps:

1.  **Check Issues** 👀: For major changes or new features, **please open an issue first** to discuss your approach.
2.  **Claim Your Task** 🙋: If you plan to work on an existing issue, **comment on it** to let others know you've claimed it.
3.  **Fork and Branch** 🌳: Fork the repository, clone your fork locally, and create a new branch for your work (e.g., `feat/disease-model` or `fix/sensor-read`).

***

## 🛠️ Development & Testing: The Essentials

### Mandatory Testing 🧪

Since we deal with AI models, stability and accuracy are critical. Any code contribution **must** be verified.

1.  **Unit Tests:** For core functions (e.g., data processing, API handling), add or update unit tests in the appropriate `tests/` directory.
2.  **Model Validation:** If you modify a core model, you must report **metrics** (e.g., accuracy, loss, F1 score) in your PR to confirm the model's performance has not degraded.
3.  Ensure all tests pass before submitting your Pull Request. **No passing tests, no merge!** 

### Code Style

Please adhere to standard Python best practices (PEP 8), and keep all dependencies updated in your `requirements.txt` (or `pyproject.toml`).

***

## 🤝 Submitting Your Pull Request (PR)

1.  **Scope:** Keep your PR focused on a single logical change.
2.  **Title:** Use a clear, brief title that reflects the change (e.g., `feat: Add support for soil moisture sensor data`).
3.  **Description:** Explain **what** you changed and **why** it benefits the project. If you updated a model, include a summary of the performance metrics.
4.  **Hacktoberfest:** Feel free to mention your participation in Hacktoberfest!

Thank you for helping Farm-IQ grow! Happy coding! 🥳

***

## 🧹 Linting (Black & isort)

To ensure a consistent code style across the repository, this project uses Black and isort. A GitHub Actions workflow (`.github/workflows/lint.yml`) automatically runs formatting checks on push and when a pull request is opened against `main`.

What the workflow does:

- Runs `black --check .` to verify code is formatted according to Black (check-only — it does not rewrite files).
- Runs `isort --check-only .` to verify imports are sorted (check-only).

How to run the checks locally:

1. (Optional) Create and activate a virtual environment:

	python -m venv .venv
	.venv\Scripts\Activate.ps1  # PowerShell on Windows

2. Install the dev tools (you can add them to `requirements-dev.txt` if you prefer):

	pip install --upgrade pip
	pip install black isort

3. Run the checks:

	black --check .
	isort --check-only .

If the checks fail, run the formatters to fix issues before committing:

	black .
	isort .

Notes:

- The GitHub Actions workflow only checks formatting to keep CI non-destructive. Please format your code locally before pushing to avoid CI failures.
- Consider using pre-commit hooks or editor integrations for automatic formatting on save; this can help reduce friction for contributors.

Pre-commit (recommended):

To automatically run Black and isort before each commit, install `pre-commit` and enable the hooks included in the repository:

1. Install pre-commit:

	pip install pre-commit

2. Install the hooks (run once per clone):

	pre-commit install

3. Optionally run hooks against all files on first setup:

	pre-commit run --all-files

This project includes a `.pre-commit-config.yaml` with Black and isort hooks. Using pre-commit reduces CI failures and keeps commits clean.
