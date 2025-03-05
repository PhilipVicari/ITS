class Account():
    def __init__(self, account_id:str,) -> None:
        self.account_id=account_id
        self.balance=0.0
    def deposit(self, amount):
        self.balance=self.balance+amount
    def get_balance(self):
        return self.balance
class Bank():
    def __init__(self) -> None:
        self.accounts={}
    def create_account(self, account_id):
        if account_id not in self.accounts:    
            account=Account(account_id)
            self.accounts[account_id] = account
            return account    
        raise ValueError("Account with this ID already exists")
    def deposit(self, account_id, amount):
        if account_id in self.accounts:
            account = self.accounts[account_id]  
            account.deposit(amount) 
            
    def get_balance(self, account_id):
        if account_id in self.accounts:
            account = self.accounts[account_id]  
            return account.get_balance() 
        raise ValueError("Account not found")



 	

bank = Bank()
account1 = bank.create_account("123")
try:
    bank.create_account("123")
except ValueError as e:
    print(e)

"""
    def deposit(self, account_id, amount):
        account = self.accounts.get(account_id)
        if account:
            account.deposit(amount)
    def get_balance(self, account_id):
        account = self.accounts.get(account_id)
        if account:
            return account.get_balance()
"""