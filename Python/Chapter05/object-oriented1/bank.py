__author__ = "ChiangWei"
__date__ = "2022/04/26"

class Account:
    pass

def account(name, number, balance):
    acct = Account()
    acct.name = name
    acct.number = number
    acct.balance = balance
    return acct

def deposit(acct, amount):
    if amount <= 0:
        print('存款金額不得為負')
    else:
        acct.balance += amount

def withdraw(acct, amount):
    if amount > acct.balance:
        print('餘額不足')
    else:
        acct.balance -= amount

def desc(acct):
    return f"Account('{acct.name}', '{acct.number}', {acct.balance})"
