class Bank_account:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(amount,'deposited.current balance',self.balance)
        else:
            print('invalid')
    def withdraw(self,amount):
        if amount>0 and self.balance>=amount:
            self.balance-=amount
            print(amount,'withdraw current balance',self.balance)
        else:
            print('invalid')
    def showbalance(self):
        print('current balance',self.balance)
class Savingsaccount(Bank_account):
    def __init__(self,balance,interest_rate):
        self.balance=balance
        self.interest_rate=interest_rate
    def add_interest(self):
        interest=self.balance*self.interest_rate/100
        self.deposit(interest)
        print('interest add',self.balance)
s=Savingsaccount(balance=1000,interest_rate=5)
s.add_interest()
s.deposit(500)
s.withdraw(200)
s.showbalance()
