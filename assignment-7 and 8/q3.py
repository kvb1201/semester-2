# Write a Python program to create a class representing a bank. Include methods for managing
# customer accounts and transactions.

class bank:
    def __init__(self):
        self.accounts = {}
        self.__pasword = {}
    
    def addAcc(self,accNo,password,balance = 0):
        self.accounts[accNo] = balance
        self.__pasword[accNo] = password

    def deposit(self,accNo,password,amount):
        if accNo in self.accounts:
            if password == self.__pasword[accNo]:
                self.accounts[accNo] += amount
                print("Balance Updated: ",self.accounts[accNo])
            else:
                print("Incorrect Password")
        else:
            print("Account Not found")

    def withdraw(self,accNo,password,amount):
        if accNo in self.accounts:
            if password == self.__pasword[accNo]:
                if self.accounts[accNo]>= amount:
                    self.accounts[accNo] -= amount
                    print("Balance Updated: ",self.accounts[accNo])
                else:
                    print("insufficient balance")
            else:
                print("Incorrect Password")
        else:
            print("Account Not found")

    def displayBalance(self,accNo,password):
        if accNo in self.accounts:
            if self.__pasword[accNo] == password:
                print(self.accounts[accNo])

b = bank()
b.addAcc(123,"abc")
b.deposit(123,"abc",100)
b.withdraw(123,'abc',90)
    

               

        