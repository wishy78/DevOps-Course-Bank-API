from dataclasses import dataclass
from datetime import datetime
from typing import Set


@dataclass(frozen=True)
class Account:
    name: str


@dataclass(frozen=True)
class Transaction:
    account: Account
    date: datetime
    amount: int


class Bank:
    def __init__(self):
        self._accounts: Set[Account] = set()
        self._transactions: Set[Transaction] = set()

    @property
    def accounts(self) -> Set[Account]:
        return self._accounts.copy()

    @property
    def transactions(self) -> Set[Transaction]:
        return self._transactions.copy()

    def create_account(self, name: str) -> Account:
        account = Account(name)
        self._accounts.add(account)
        return account

    def get_account(self, name: str) -> Account:
        for account in self.accounts:
            if account.name == name:
                return account
        raise ValueError('Account not found')

    def add_funds(self, name: str, amount: int) -> None:
        account = self.get_account(name)
        now = datetime.now()
        self._transactions.add(Transaction(account, now, amount))
