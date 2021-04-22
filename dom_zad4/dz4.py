class BankAccount:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        return f"My account's number {self._name}"

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def balance(self):
        return f"user account: {self._balance} Euro"

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError("System error!")
        self._balance = balance

account = BankAccount(1, 90)
account.name = 1004199510
print(account.name)

account.balance = 10000
print(account.balance)