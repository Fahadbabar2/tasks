class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Not enough balance")

    def check_balance(self):
        print("Balance:", self.balance)

account = BankAccount(1000)
account.deposit(200)
account.withdraw(500)
account.check_balance()
