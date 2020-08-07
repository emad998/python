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



class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 20, balance = 0)

    def make_deposit(self, amount):
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(self.name, self.account.balance)
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty python", "monty@python.com")
emad = User("Emad hanna", "emad@python.com")




guido.make_deposit(100).make_withdrawal(50).account.yield_interest().display_account_info()
