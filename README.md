# Python API Testing Practice

Educational API testing exercises using Python, pytest and Requests, originally completed during QA Studio training in September 2025. The repository was reorganized in November 2026 with AI-assisted safety and documentation improvements. This is a practice project, not a production test framework or evidence of commercial automation experience.

## What is included

- `RequestsTest2/tests/test_pokemons.py`: GET request checks for Pokémon and trainers, HTTP status assertions, response field checks and pytest parametrization.
- `RequestsTest2/main.py`: examples of registration, email confirmation, Pokémon creation, updating Pokémon and adding a Pokémon to a Pokéball. These examples are not automated assertions and are never executed on import.
- `requirements.txt`: Python dependencies.
- `.env.example`: optional configuration variable reference; no real credentials.

Target: the QA Studio Pokémon Battle training API at https://api.pokemonbattle.ru/v2.

## Getting started

Python 3.10+ is recommended. Install dependencies in a virtual environment:

```bash
python -m venv .venv
```

Activate it (PowerShell: `.\.venv\Scripts\Activate.ps1`; macOS/Linux: `source .venv/bin/activate`), then run:

```bash
python -m pip install -r requirements.txt
python -m pytest --collect-only -q
```

## Running the tests

```bash
python -m pytest -q
```

The trainer-list status test needs a reachable training API. The remaining tests require your own training data. Set environment variables using your shell (PowerShell example):

```powershell
$env:POKEMON_TRAINER_ID = "your-trainer-id"
$env:POKEMON_ID = "your-pokemon-id"
$env:POKEMON_NAME = "your-pokemon-name"
$env:POKEMON_TRAINER_NAME = "your-trainer-name"
python -m pytest -q
```

Tests that require missing configuration are skipped. The optional `POKEMON_API_TOKEN` is used for authenticated request examples, not for the original GET checks. The `.env.example` file is a reference only; it is not automatically loaded.

The tests still depend on an external training service and existing account data. They are not a self-contained or guaranteed deterministic suite. No live API test results are claimed for this migrated version.

## Security

Do not commit credentials, tokens, real account details, local environment files or generated Python bytecode. Mutating API examples in `main.py` must be called explicitly and should only be used with your own authorized training account.
