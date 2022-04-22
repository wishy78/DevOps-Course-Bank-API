"""Integration tests for app.py"""
from typing import Type
from flask.testing import FlaskClient
from flask.wrappers import Response
import pytest

from bank_api.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


def test_account_creation(client: FlaskClient):
    # Use the "client" object to make requests e.g. making a POST request:
    # response = client.post('/some/path')
    
    # Or to make a GET request:
    # client.get('/some/path')
    
    # Documentation: https://flask.palletsprojects.com/en/2.1.x/testing/
    pass
