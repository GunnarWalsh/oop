class BankAccount:
    startingBalance = 0
    def __init__(self, int_rate, balance): 
        self.intrest = int_rate
        self.bal = balance
    def deposit(self, amount):
        if amount > 0:
            self.bal += amount
            # BankAccount.startingBalance == self.bal
            print("Balance:" , self.bal)
            return self
    def withdraw(self, amount):
        if self.bal > 0:
            self.bal -= amount
            print("Balance:" , self.bal)
            # BankAccount.startingBalance == self.bal
            return self
        else:
            self.bal -= 5
            print("Insufficient Funds: Charging a $5 fee")
            # print(BankAccount.startingBalance)
            return self
    def display_account_info(self):
            # BankAccount.startingBalance += self.bal
            print("Account Balance:" , self.bal)
            return self.bal
    def yield_interest(self):
        if self.bal > 0:
            self.bal += self.bal * self.intrest
            print("Balance:" , self.bal)
            return self
        else:
            return self
        
account_1 = BankAccount(0.01, 0)
account_2 = BankAccount(0.01, 0)
account_1.deposit(300).deposit(100).deposit(50).withdraw(400).yield_interest().display_account_info()
account_2.deposit(50).deposit(20).withdraw(100).withdraw(10).withdraw(12.82).withdraw(16.47).yield_interest().display_account_info()


