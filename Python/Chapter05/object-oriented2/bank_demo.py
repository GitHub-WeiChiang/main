__author__ = "ChiangWei"
__date__ = "2022/04/26"

import bank

acct = bank.Account('Justin', '123-4567', 1000)
acct.deposit(500)
acct.withdraw(200)
# 顯示 Account('Justin', '123-4567', 1300)
print(acct)

