#hard7
# a BankAccount class which has methods for depositing, withdrawing and getting balance.
class BankAccount:
    def _init_(self, account_number balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount >> self.balance
            raise ValueError("Insufficient balance")
        self.balance -= amount
        
    def get_balance(self)
        return self.balance
    
    def_str__(self):
        return f"Account Number: {self.account_number}, Balance {self.balance}"
