from Storage import all_accounts
from ErrorHandling import AmountDepositError, AmountWithdrawError

def findAccountByAccountNumber(acc_number):
    for account in all_accounts:
        if acc_number == account.account_number:
            return account
    return None

def findAccountByUsername(username):
    """Find account by username"""
    for account in all_accounts:
        if account.username == username:
            return account
    return None

def depositAmount(account):
    # Bug Fix: Wrapped in try-except to catch invalid numeric letters input
    try:
        amount = int(input('Enter amount to deposit: '))
        account.deposit(amount)
    except ValueError:
        print('Error: Invalid numeric input.')
    except AmountDepositError as e:
        print(e)

def withdrawAmount(account):
    try:
        amount = int(input('Enter amount to withdraw: '))
        account.withdraw(amount)
    except ValueError:
        print('Error: Invalid numeric input.')
    except AmountWithdrawError as e:
        print(e)

def showAccountDetails(account):
    account.show_details()       