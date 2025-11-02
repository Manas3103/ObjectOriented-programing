from Bank_Account import *

Dave = BankAccount(1000,"Dave")
Sara = BankAccount(2000,"Sara")

Dave.getBalance()
Sara.getBalance()

Dave.deposit(500)
Sara.deposit(1500)

Dave.withdraw(10000)
Sara.withdraw(700)

Sara.transfer(250,Dave)
Sara.transfer(25000,Dave)

Manas = InterestRewardsAcct(2000, "Manas")

Manas.deposit(10000)
print(type(Manas))
Manas.transfer(50,Dave)

