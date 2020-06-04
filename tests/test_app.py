"""Integration tests for app.py"""
import json

import pytest

from bank_api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_create_account(client):
    """I should be able to create, then query an account"""
    response_creation = client.post('/accounts/test')
    response_query = client.get('/accounts/test')

    assert response_creation.status_code == 200
    assert response_query.status_code == 200

    data = json.loads(response_query.data)
    assert data['name'] == 'test'


def test_get_invalid_account_fails_with_404(client):
    """Querying a non-existant account returns 404 (Not Found)"""
    response_query = client.get('/accounts/nothere')
    assert response_query.status_code == 404
