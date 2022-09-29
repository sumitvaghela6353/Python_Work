class Account:
     def __init__(self):
          self.balance = 0
          print("\n Hello Sumit Vaghela, Welcome to the Deposit & Withdrawal Machine")

     def deposit(self):
          amount = int(input("\n Enter amount to be deposted: "))
          self.balance += amount
          print("your deposit ammount is:", self.balance)

     def withdraw(self):
          amount = int(input("Enter amount to be Withdrawn: "))
          if self.balance >= amount:
               self.balance -= amount
               print("\n You Withdrew:", amount)
          else:
               print("\n Insufficient balance  ")
          
     def display(self):
               print("Available balance is:", self.balance)
 
a = Account()         
a.deposit()
a.withdraw()
a.display()
a.deposit()
a.withdraw()
a.display()