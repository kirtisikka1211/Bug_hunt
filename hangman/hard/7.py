class BankAccount:
    def __init__(self, account_number balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance
            raise ValueError("Insufficient balance")
        self.balance -= amount
        
    def get_balance(self):
        return self.balance
    
    def_str__(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"


# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError("Insufficient balance")
#         self.balance -= amount

#     def get_balance(self):
#         return self.balance

#     def __str__(self):
#         return f"Account Number: {self.account_number}, Balance: {self.balance}"
