__author__ = "ChiangWei"
__date__ = "2022/04/26"

def account(name: str, number: str, balance: float) -> dict:
    return {'name': name, 'number': number, 'balance': balance}

def deposit(acct, amount):
    if amount <= 0:
        print('存款金額不得為負')
    else:
        acct['balance'] += amount

def withdraw(acct, amount):
    if amount > acct['balance']:
        print('餘額不足')
    else:
        acct['balance'] -= amount

def desc(acct):
    return f'Account:{acct}'
