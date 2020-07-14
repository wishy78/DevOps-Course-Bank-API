# Bank API

This is a standalone exercise to practice writing tests and engaging in Test Driven Development (TDD).

## Setup

This project requires Python 3.7 and uses Poetry for Python to handle dependencies. Follow the instructions 
[here](https://python-poetry.org/docs/#installation) to set up Poetry.

If this is the first time you're using poetry you'll want to run 

`$ poetry config virtualenvs.in-project true`

This will insure that running `poetry install` below will install the virtual environment in the project root (rather than in `~/.poetry`)

Once configured, the following command (run from the project root) will install project dependencies:

`$ poetry install`

VSCode should then detect the newly create `.venv` folder and prompt to select the interpreter from there.

To launch the API, run the `app.py` file from within the poetry shell by running the following:

```bash
$ cd bank_api
$ flask run
```

The API should be live with swagger docs visible at http://localhost:5000/.

## Tests

You can run both unit and integration tests suites using pytest:
1. `poetry shell` (if not already active)
2. `pytest`

However if you'd like to run/debug tests individually you can run:

`Ctrl/Cmd + Shift + P` => `Discover Tests`.

Tests will then appear by clicking the beaker icon on the activity bar on the left edge of VSCode.
* Intellisense annotations for running/debugging each test should also appear above the test functions in the code.