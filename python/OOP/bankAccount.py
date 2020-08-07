class BankAccount:
    def __init__(self, int_rate, balance):
       
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"your interest rate is {self.int_rate}, and your balance is {self.balance}")
        return self

    def yield_interest(self):
        self.balance += 20
        return self

account_1 = BankAccount( 20, 0)    
account_2 = BankAccount( 20, 0)

account_1.deposit(100).deposit(100).deposit(100).yield_interest().display_account_info()
account_2.deposit(700).deposit(200).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()