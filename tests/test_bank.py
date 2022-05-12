"""Unit tests for bank.py"""

from datetime import datetime
import pytest

from bank_api.bank import Account, Bank, Transaction


@pytest.fixture
def bank() -> Bank:
    return Bank()

def test_create_account_raises_error_if_name_blank(bank: Bank):
    # This means: assert an exception is raised during the following block
    with pytest.raises(Exception):
        bank.create_account('')

def test_bank_creates_empty(bank: Bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0

def test_can_create_and_get_account(bank: Bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'

def test_get_account_raises_error_if_no_account_matches(bank: Bank):
    bank.create_account('Name 1')

    # This means: assert an exception is raised during the following block
    with pytest.raises(ValueError):
        bank.get_account('Name 2')

@pytest.mark.freeze_time
def test_add_funds_transaction(bank: Bank):
    bank.create_account('Name 3')
    bank.add_funds('Name 3',20)
    # This means: assert an exception is raised during the following block

    transaction = bank.transactions[0]
    assert len(bank.transactions) == 1
    assert transaction.account.name == 'Name 3'
    assert transaction.amount == 20
    assert transaction.date == datetime.now()
# test for disallowed adding funds to none exsiting account
def test_add_funds_Exception_Capture(bank: Bank):
    with pytest.raises(ValueError):
        bank.add_funds('Name 4',20)
# test for disallowed negative
def test_add_funds_neg_value(bank: Bank):
    bank.create_account('Name 5')
    with pytest.raises(ValueError):
        bank.add_funds('Name 5',-1)        
# test for disallowed zero
def test_add_funds_zero_value(bank: Bank):
    bank.create_account('Name 6')
    with pytest.raises(ValueError):
        bank.add_funds('Name 6',0)  
# test for disallowed decimal
def test_add_funds_decimal_value(bank: Bank):
    bank.create_account('Name 7')
    with pytest.raises(ValueError):
        bank.add_funds('Name 7',1.50)  

# Must be an int
# cnanot be 0 or negative


# TODO: Add unit tests for bank.add_funds()

