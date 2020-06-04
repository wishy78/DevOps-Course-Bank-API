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


def test_get_balance(client):
    account_name = 'balance_test'
    create = client.post(f'/accounts/{account_name}')
    before = client.get(f'/accounts/{account_name}')
    move = client.post('/money', data=dict(
        name=account_name,
        amount=50
    ))
    after = client.get(f'/accounts/{account_name}')

    assert create.status_code == 200
    assert before.status_code == 200
    assert move.status_code == 200
    assert after.status_code == 200

    balance_before = json.loads(before.data)['balance']
    balance_after = json.loads(after.data)['balance']

    assert balance_before == 0
    assert balance_after == 50
