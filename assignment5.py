# This is a basic banking application

class BankAccount:
    def __init__(self, account_number, balance, owner, type):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type

    def __str__(self):
        return "Account owner: {}\nAccount number: {}\nAccount type: {}\nAccount balance: UGX.{}".format(self.owner, self.account_number,self.type, self.balance)
        

class Bank:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts
    
    def __str__(self):
        return f"Bank Name: {self.name}\n**List of accounts** \n{self.accounts}"
        

class Customer:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts

    def __str__(self):
        return f"Customer: {self.name}\n *Account details*\n{self.accounts}"
        
        
class Transactions:
    def __init__(self, account, amount, type):
        self.account = account
        self.amount = amount
        self.type = type
    
    def transaction(self, amount_):

        current_balance = self.amount
        print(f"Current balance: {current_balance}")

        if self.type == 'withdraw':
            current_balance -= amount_
            return f"New balance: {current_balance}"
        elif self.type == 'deposit':
            current_balance += amount_
            return f"New balance: {current_balance}"
    

# customer object
b = BankAccount(7869858694, 54600.0, 'Charles Darren', 'Saving') 
print(b)
# bank object
g = Bank("Stanbic", b)
print(g)
# customer object
c = Customer("Charles Wagaana", b)
print(c)

t = Transactions(7869858694, 54600.0, 'deposit')
print(t.transaction(10000.0))
print(b)

        