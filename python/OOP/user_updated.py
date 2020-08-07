class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty python", "monty@python.com")
emad = User("Emad hanna", "emad@python.com")


guido.make_deposit(100).make_deposit(300).make_withdrawal(100).make_withdrawal(100).transfer_money(emad, 200)




monty.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100)



emad.make_deposit(300).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100)



monty.display_user_balance()
guido.display_user_balance()
emad.display_user_balance()