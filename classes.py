import random


class BankAccount():
    
    def __init__(self, owner, balance = 0, has_overdraft = False):
        self.owner = owner
        self.balance = balance
        self.account_no  = random.randint(111111111, 999999999)
        self.has_overdraft = has_overdraft

    def deposit(self , amount):
        
        if isinstance(amount, (int,float)) and not isinstance(amount,bool):

							   
            self.balance += amount
            return f"Account {self.account_no} - New balance: {self.balance} $$"
        else:
            return f"please enter a valid input"
							   
    def withdraw(self , amount):
        
        if isinstance(amount, (int,float)) and not isinstance(amount,bool):
            
            if self.has_overdraft == False:
                
                if self.balance >= amount:
                    self.balance -= amount
                    return f"Account {self.account_no} - New balance: {self.balance} $$"
                else:
                    return f"insufficient balance to withdraw {amount} $$ Account Balance: {self.balance} $$ "
            elif self.has_overdraft == True:
                self.balance -= amount
                return f"Account {self.account_no} - New balance: {self.balance} $$"
            
        else:
            return f"please enter a valid input"
        
    def __str__(self):
       return f"Account {self.account_no} - Balance: {self.balance} $$"
   
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        return "No withdrawals permitted"
   
# account1								  
account1 = BankAccount("Charlie", 78)

print(account1)
print(account1.deposit(200))
print(account1.withdraw(25))
print(account1.withdraw(50))

# account2
account2 = BankAccount("Bob", 500)

print(account2)
print(account2.deposit(1000))
print(account2.withdraw(4000))
print(account2.deposit(200))


# SavingsAccount
savings = SavingsAccount("Jack", 20000)

print(savings)
print(savings.deposit(1000))
print(savings.withdraw(1500))