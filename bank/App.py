from Bank import Bank
from Storage import all_accounts
from Functions import findAccountByAccountNumber, depositAmount, withdrawAmount, showAccountDetails

while True:
    print('\nWelcome to Bank Application')
    print('1. Create Account')
    print('2. Deposit Balance')
    print('3. Withdraw Balance')
    print('4. Show Details')
    print('5. Exit')

    try:
        choice = int(input('Enter your choice (1 - 5): '))
    except ValueError:
        print('Error: Please enter a valid number.')
        continue

    if choice == 1:
        y_n = input('Do you really want to create new account (y/n)? ').lower()
        if y_n == 'y':
            name = input('Enter your name: ').strip()
            if not name:
                print("Error: Name cannot be blank.")
                continue
            try:
                balance = int(input('Enter your initial balance: '))
                if balance >= 0:
                    b = Bank(name, balance)
                    all_accounts.append(b)
                    print(f'Account created for {name} with balance Rs.{balance} and A/C no. {b.account_number}.')
                else:
                    print('Error: Initial balance cannot be negative.')
            except ValueError:
                print('Error: Balance must be a numeric value.')
        else:
            print('Continuing with your transaction.')

    elif choice in [2, 3, 4]:
        acc_number = input('Enter your account number: ').strip()
        find_acc = findAccountByAccountNumber(acc_number)
        
        if find_acc:
            if choice == 2:
                y_n = input('Do you really want to deposit balance (y/n)? ').lower()
                if y_n == 'y':
                    depositAmount(find_acc)
            elif choice == 3:
                y_n = input('Do you really want to withdraw balance (y/n)? ').lower()
                if y_n == 'y':
                    withdrawAmount(find_acc)
            elif choice == 4:
                showAccountDetails(find_acc)
        else:
            print('Account number does not match') 

    elif choice == 5:
        print('Thank you for choosing us.')
        break
    else:
        print('Error: Invalid Input. Enter valid input from 1 to 5.')