# Contributing to Movewell Family

Thank you for your interest in contributing to **Movewell Family**! We welcome contributions from developers, researchers, physical therapists, and open-source enthusiasts.

## Code of Conduct
We are committed to providing a welcoming and inclusive environment. Please treat all contributors with respect and professionalism.

## How Can I Contribute?

### 1. Reporting Bugs
- Search existing issues to ensure the bug hasn't already been reported.
- Open a new issue with a clear title, reproducible steps, expected vs. actual behavior, and environment details.

### 2. Suggesting Enhancements
- Open an issue tagged as `enhancement` describing the proposed feature and why it benefits the Movewell Family community.

### 3. Pull Requests (PRs)
1. Fork the repository and create your feature branch: `git checkout -b feature/my-amazing-feature`.
2. Ensure your code follows Python PEP 8 standards and TypeScript ESLint conventions.
3. Write clean, self-documenting code with unit tests.
4. Verify that all tests pass locally:
   ```bash
   pytest movewell_engine/tests
   ```
5. Commit your changes with clear, descriptive messages following conventional commits (`feat: ...`, `fix: ...`, `docs: ...`).
6. Push to your branch and submit a Pull Request.

## Development Setup

1. **Backend Engine Setup:**
   ```bash
   cd movewell_engine
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Vision Service Setup:**
   ```bash
   cd movewell_vision
   npm install
   npm run build
   ```

## Security & Secrets
Do **NOT** commit hardcoded secrets, private tokens, passwords, or personal health info (PHI). Use `.env` files locally and environment variables in production.
