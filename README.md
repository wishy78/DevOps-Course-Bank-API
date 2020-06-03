# TDD Exercise

This is a standalone exercise to practice writing tests and engaging in Test Driven Development (TDD).

## Setup

This project requires Python 3.6 and uses Poetry for Python to handle dependencies. Follow the instructions 
[here](https://python-poetry.org/docs/#installation) to set up Poetry.

Once configured, the following commands (run from the project root) will install project dependencies:
1. `poetry shell`
2. `poetry install`

To launch the API, run the `app.py` file from within the poetry 
shell. The API should be live and swagger docs visible at http://localhost:5000/.

## Tests

Unit and integration tests suits are run using pytest:
1. `poetry shell` (if not already active)
2. `pytest`
