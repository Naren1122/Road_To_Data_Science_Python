import random
import hashlib
from ErrorHandling import AmountDepositError, AmountWithdrawError

class Bank:
    def __init__(self, account_name, initial_balance, username, password):
        self.account_name = account_name
        self.balance = initial_balance  # Changed from initial_balance to track dynamic updates
        self.account_number = "".join(str(random.randint(0, 9)) for _ in range(16))
        self.username = username
        # Hash the password for security
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        """Check if the provided password matches the stored hash"""
        return hashlib.sha256(password.encode()).hexdigest() == self.password_hash

    def login(self, username, password):
        """Authenticate user with username and password"""
        return self.username == username and self.check_password(password)

    def deposit(self, amount):
        if amount > 0:  # Enforces non-negative enforcement as required
            self.balance += amount
            print(f'Rs.{amount:.2f} has been deposited to A/C no. {self.account_number}.')
        else:
            raise AmountDepositError('Error: Deposit amount must be greater than zero.')

    def withdraw(self, amount):
        if amount <= 0:
            raise AmountWithdrawError('Error: Withdraw amount must be greater than zero.')
        
        # Bug Fix: Changed from '<' to '<=' to allow withdrawing total balance
        if amount <= self.balance:
            self.balance -= amount
            print(f'Rs.{amount:.2f} has been withdrawn from A/C no. {self.account_number}.')
        else:
            raise AmountWithdrawError('Error: Withdraw amount must be less than or equal to balance amount.')

    def show_details(self):
        print("\n--- Account Details ---")
        print(f'Account Name: {self.account_name}')
        print(f'Account Number: {self.account_number}')
        print(f'Current Balance: Rs.{self.balance:.2f}')
        print("-----------------------")
