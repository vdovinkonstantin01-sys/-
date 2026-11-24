class Account:
    def __init__(self, number, owner, balance=0):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.number = number
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount

    def __repr__(self):
        return f"Account({self.number!r}, {self.owner!r}, {self._balance!r})"


class SavingsAccount(Account):
    def __init__(self, number, owner, balance=0, rate=0.05):
        super().__init__(number, owner, balance)
        self.rate = rate

    def add_interest(self):
        self._balance += self._balance * self.rate

    def __repr__(self):
        return (
            f"SavingsAccount({self.number!r}, {self.owner!r}, "
            f"{self._balance!r}, {self.rate!r})"
        )


class CheckingAccount(Account):
    def __init__(self, number, owner, balance=0, overdraft=0):
        super().__init__(number, owner, balance)
        if overdraft < 0:
            raise ValueError("Овердрафт не может быть отрицательным")
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if self._balance - amount < -self.overdraft:
            raise ValueError("превышен овердрафт")
        self._balance -= amount

    def __repr__(self):
        return f"CheckingAccount({self.number!r}, {self.owner!r}, {self._balance!r})"


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self._accounts = []

    def add_account(self, account):
        self._accounts.append(account)

    def remove_account(self, number):
        for i, acc in enumerate(self._accounts):
            if acc.number == number:
                self._accounts.pop(i)
                return
        raise KeyError("Счёт не найден")

    def accounts(self):
        return list(self._accounts)

    def total_balance(self):
        return sum(acc.balance for acc in self._accounts)


class Bank:
    def __init__(self):
        self._customers = {}
        self._accounts = {}
        self._account_owners = {}

    def add_customer(self, customer):
        if customer.customer_id in self._customers:
            raise ValueError("Клиент с таким ID уже существует")
        self._customers[customer.customer_id] = customer
        for acc in customer.accounts():
            if acc.number in self._accounts:
                raise ValueError("Номер счёта уже существует в банке")
            self._accounts[acc.number] = acc
            self._account_owners[acc.number] = customer

    def customer(self, customer_id):
        if customer_id not in self._customers:
            raise KeyError("Клиент не найден")
        return self._customers[customer_id]

    def open_account(self, customer_id, account):
        cust = self.customer(customer_id)
        if account.number in self._accounts:
            raise ValueError("Номер счёта уже занят")
        self._accounts[account.number] = account
        self._account_owners[account.number] = cust
        cust.add_account(account)

    def close_account(self, number):
        if number not in self._accounts:
            raise KeyError("Счёт не найден")
        account = self._accounts[number]
        if account.balance != 0:
            raise ValueError("На счёте есть деньги")
        owner = self._account_owners.pop(number)
        self._accounts.pop(number)
        owner.remove_account(number)

    def transfer(self, from_number, to_number, amount):
        if from_number not in self._accounts or to_number not in self._accounts:
            raise KeyError("Счёт не найден")
        if from_number == to_number:
            raise ValueError("Перевод на тот же счёт")
        source = self._accounts[from_number]
        target = self._accounts[to_number]
        source.withdraw(amount)
        target.deposit(amount)

    def accounts(self, customer_id, min_balance=None):
        cust_accounts = self.customer(customer_id).accounts()
        if min_balance is None:
            return cust_accounts
        return [acc for acc in cust_accounts if acc.balance >= min_balance]

    def total_deposits(self):
        return sum(acc.balance for acc in self._accounts.values())


if __name__ == "__main__":
    pass
