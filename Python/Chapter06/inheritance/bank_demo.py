__author__ = "ChiangWei"
__date__ = "2022/04/28"

import bank

savingsAcct = bank.SavingsAccount('Justin', '123-4567', 1000, 0.02)

savingsAcct.deposit(500)
savingsAcct.withdraw(200)

print(savingsAcct)
