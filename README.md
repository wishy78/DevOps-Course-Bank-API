# Bank API

This is a standalone exercise to practice writing tests and engaging in Test Driven Development (TDD).

## Setup

This project requires Python 3.7 and uses Poetry for Python to handle dependencies. Follow the instructions 
[here](https://python-poetry.org/docs/#installation) to set up Poetry.

Run the following command (run from the project root) to install project dependencies:

`$ poetry install`

VSCode should then detect the newly create `.venv` folder and prompt to select the interpreter from there

To launch the API, run the following:

```bash
$ cd bank_api
$ poetry run flask run
```

If you open a poetry shell with the command `poetry shell` then you do not need to preface your commands with "poetry run". E.g. you can execute `flask run` directly

The API should be live with swagger docs visible at http://localhost:5000/.

## Tests

You can run both unit and integration tests suites using pytest:
1. `poetry shell` (if not already active)
2. `pytest` (from the root directory)

However if you'd like to run/debug tests individually you can run:

`Ctrl/Cmd + Shift + P` => `Discover Tests`.

Tests will then appear by clicking the beaker icon on the activity bar on the left edge of VSCode.
* Intellisense annotations for running/debugging each test should also appear above the test functions in the code.