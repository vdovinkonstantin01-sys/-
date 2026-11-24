class Account:
    def __init__(self, number, owner, balance=0):
        if balance < 0:
            raise ValueError
        self._number = number
        self._owner = owner
        self._balance = balance

    @property
    def number(self):
        return self._number

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError
        if amount > self._balance:
            raise ValueError
        self._balance -= amount

    def __repr__(self):
        return f"Account('{self._number}', '{self._owner}', {self._balance})"


if __name__ == "__main__":
    pass
