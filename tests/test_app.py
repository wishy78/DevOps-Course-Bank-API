"""Integration tests for app.py"""
from typing import Type
from flask.testing import FlaskClient
from flask.wrappers import Response
import pytest

from bank_api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_account_creation(client: FlaskClient):

    response = client.post('/accounts/qwerty')
    assert response.status_code == 200
    assert response.json['name'] == 'qwerty'

    response = client.get('/accounts/qwerty')
    assert response.status_code == 200
    assert response.json['name'] == 'qwerty'
    
