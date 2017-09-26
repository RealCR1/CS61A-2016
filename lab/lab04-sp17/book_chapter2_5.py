class Account:
    interest = 0.02
    def __init__(self, account_holder):
        #Oh, it is so important to type two '_' at the both siede of the function.
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        if self.balance < amount:
            return 'Insufficient funds.'
        else:
            self.balance = self.balance - amount
            return self.balance

class CheckingAccount(Account):
    """
    A bank account that charges for withdrawls.
    """
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)


class SavingsAccount(Account):
    """
    A bank account that charges for deposit.
    """
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    """docstring for AsSeenOnTVAccount"""
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1


"""
subclass points to the base class.From AsSeenOnTVAccount-->CheckingAccount -->SavingsAccount
--> Account -->object
"""



        