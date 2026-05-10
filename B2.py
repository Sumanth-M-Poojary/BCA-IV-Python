# Base class for bank account
class BankAccount:
    def __init__(self):
        # Initialize balance to 0
        self.balance = 0

    def deposit(self, amount):
        # Add money to account if amount is valid
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        # Withdraw money if valid and enough balance exists
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}")

    def get_balance(self):
        # Display current balance
        print(f"Balance: ₹{self.balance}")


# Derived class for savings account
class SavingsAccount(BankAccount):
    def __init__(self):
        # Call parent constructor
        super().__init__()
        # Initialize interest rate
        self.rate = 0

    def set_rate(self, rate):
        # Set interest rate if valid
        if rate >= 0:
            self.rate = rate
            print(f"Interest rate set to {rate}%")
        else:
            print("Invalid rate")

    def add_interest(self):
        # Calculate and add interest to balance
        interest = self.balance * self.rate / 100
        self.balance += interest
        print(f"Interest added: ₹{interest}")


# Create account object
acc = SavingsAccount()

# Menu-driven program
while True:
    # Display options
    print("\n1.Deposit  2.Withdraw  3.Balance  4.Set Rate  5.Add Interest  6.Exit")
    choice = input("Choose: ")

    # Perform operations based on user choice
    if choice == "1":
        acc.deposit(float(input("Amount: ")))

    elif choice == "2":
        acc.withdraw(float(input("Amount: ")))

    elif choice == "3":
        acc.get_balance()

    elif choice == "4":
        acc.set_rate(float(input("Rate: ")))

    elif choice == "5":
        acc.add_interest()

    elif choice == "6":
        # Exit program
        print("Exiting...")
        break

    else:
        print("Invalid choice")