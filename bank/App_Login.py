from Bank import Bank
from Storage import all_accounts
from Functions import findAccountByAccountNumber, depositAmount, withdrawAmount, showAccountDetails

# Track the current logged-in user
current_user = None

def findAccountByUsername(username):
    """Find account by username"""
    for account in all_accounts:
        if account.username == username:
            return account
    return None

def signup():
    """Handle new user registration"""
    print("\n--- Create New Account ---")
    name = input('Enter your name: ').strip()
    if not name:
        print("Error: Name cannot be blank.")
        return

    username = input('Choose a username: ').strip()
    if not username:
        print("Error: Username cannot be blank.")
        return

    # Check if username already exists
    if findAccountByUsername(username):
        print("Error: Username already exists. Please choose a different one.")
        return

    password = input('Choose a password: ').strip()
    if not password:
        print("Error: Password cannot be blank.")
        return

    try:
        balance = int(input('Enter your initial balance: '))
        if balance >= 0:
            b = Bank(name, balance, username, password)
            all_accounts.append(b)
            print(f'Account created for {name} with balance Rs.{balance} and A/C no. {b.account_number}.')
            print(f'Your username is: {username}')
        else:
            print('Error: Initial balance cannot be negative.')
    except ValueError:
        print('Error: Balance must be a numeric value.')

def login():
    """Handle user login"""
    global current_user
    print("\n--- Login ---")
    username = input('Enter your username: ').strip()
    password = input('Enter your password: ').strip()

    account = findAccountByUsername(username)
    if account and account.login(username, password):
        current_user = account
        print(f'Welcome back, {account.account_name}!')
        return True
    else:
        print('Error: Invalid username or password.')
        return False

def logout():
    """Handle user logout"""
    global current_user
    if current_user:
        print(f'Goodbye, {current_user.account_name}!')
        current_user = None
    else:
        print('You are not logged in.')

# Main application loop
while True:
    print('\nWelcome to Bank Application')

    # Show different menus based on login status
    if current_user:
        print(f'Logged in as: {current_user.username}')
        print('1. Deposit Balance')
        print('2. Withdraw Balance')
        print('3. Show Details')
        print('4. Logout')
        print('5. Exit')

        try:
            choice = int(input('Enter your choice (1 - 5): '))
        except ValueError:
            print('Error: Please enter a valid number.')
            continue

        if choice == 1:
            y_n = input('Do you really want to deposit balance (y/n)? ').lower()
            if y_n == 'y':
                depositAmount(current_user)
        elif choice == 2:
            y_n = input('Do you really want to withdraw balance (y/n)? ').lower()
            if y_n == 'y':
                withdrawAmount(current_user)
        elif choice == 3:
            showAccountDetails(current_user)
        elif choice == 4:
            logout()
        elif choice == 5:
            print('Thank you for choosing us.')
            break
        else:
            print('Error: Invalid Input. Enter valid input from 1 to 5.')
    else:
        print('1. Sign Up')
        print('2. Login')
        print('3. Exit')

        try:
            choice = int(input('Enter your choice (1 - 3): '))
        except ValueError:
            print('Error: Please enter a valid number.')
            continue

        if choice == 1:
            signup()
        elif choice == 2:
            login()
        elif choice == 3:
            print('Thank you for choosing us.')
            break
        else:
            print('Error: Invalid Input. Enter valid input from 1 to 3.')
