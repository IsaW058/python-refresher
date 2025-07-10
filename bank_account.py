class Bankaccount:
    def __init__(self, name, balance, account_number):
        """Initialize a new bank account.

        This function"""
        self.name = name
        self.balance = balance
        self.account_number = account_number

    def withdraw(self, amount):
        """Withdraw money from balance.

        This function takes a float input 'amount' and returns the account balance after withdrawing the specified amount.
        The amount withdrawn must be less than or equal to the account and more than 0, or else it will return a False bool.
        """
        if amount > self.balance or amount < 0:
            return False
        self.balance = self.balance - amount
        return True

    def deposit(self, amount):
        """Deposit money into account.

        This function takes a float input 'amount' and returns the balance after depositing the specified amount.
        The amount deposited must be positive, or else it will return a False bool."""
        if amount < 0:
            return False
        self.balance = self.balance + amount
        return True

    def print_balance(self):
        """Print balance."""
        print(f"Balance: + {self.balance}")

    # def deposit(self, amount):
    #     self.balance -= amount

    # def withdraw(self, amount):
    #     self.
