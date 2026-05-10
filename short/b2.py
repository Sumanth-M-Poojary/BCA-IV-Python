""" Write a program menu driven to create a BankAccount class. class should support the following 
methods for  
i) Deposit 
ii) Withdraw
iii) GetBalanace  
Create a  subclass  SavingsAccount class that behaves just like a BankAccount, but also has an 
interest rate and a method that increases the balance by the appropriate amount of interest.    
"""
# Parent class
class BankAccount:

    # Constructor
    def __init__(self):
        self.balance = 0

    # Deposit money
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    # Withdraw money
    def withdraw(self, amount):

        # Check balance
        if amount > self.balance:
            print("Insufficient Balance")

        else:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)

    # Show balance
    def show_balance(self):
        print("Balance:", self.balance)


# Child class
class SavingsAccount(BankAccount):

    # Constructor
    def __init__(self):
        super().__init__()
        self.rate = 0

    # Set interest rate
    def set_rate(self, rate):
        self.rate = rate

    # Add interest
    def add_interest(self):

        interest = (self.balance * self.rate) / 100

        self.balance = self.balance + interest

        print("Interest Added:", interest)


# Create object
acc = SavingsAccount()


# Menu
while True:

    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.Show Balance")
    print("4.Set Interest Rate")
    print("5.Add Interest")
    print("6.Exit")

    ch = input("Enter Choice: ")

    # Deposit
    if ch == "1":

        amt = float(input("Enter Amount: "))
        acc.deposit(amt)

    # Withdraw
    elif ch == "2":

        amt = float(input("Enter Amount: "))
        acc.withdraw(amt)

    # Balance
    elif ch == "3":

        acc.show_balance()

    # Set rate
    elif ch == "4":

        r = float(input("Enter Rate: "))
        acc.set_rate(r)

    # Add interest
    elif ch == "5":

        acc.add_interest()

    # Exit
    elif ch == "6":

        print("Exiting...")
        break

    else:
        print("Invalid Choice")