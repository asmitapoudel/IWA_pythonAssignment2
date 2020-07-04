"""banking application class example
"""

class Customer:
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    def create_account(self):
        account = 555912365487
        self.account = account
        print("Account {} is created for {}".format(self.account,self.name))

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

c = Customer("Shyam")
c.create_account()