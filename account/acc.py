class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = float(file.read())

    def withdraw(self, amt):
        self.balance = self.balance - amt
        account.commit()

    def deposit(self, amt):
        self.balance = self.balance + amt
        account.commit()

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


#Remember to pass the name of the base class it is
#expected to inherit from as a parameter
class Checking(Account):
    #Essentially the Checking class inherits the init from Account
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amt):
        self.balance = self.balance - amt - self.fee
        account.commit()


#Here you need to pass the filepath for the class whatever it may be.
account = Account("balance.txt")
#This output should be a hexadecimal value
#indication the location of the object in memory
#print(account)
#To get the balance or value you need to use the dot notation.
#print(account.balance)
#account.withdraw(500.00)
#account.deposit(50.00)
#account.deposit(250.00)
print(account.balance)
checking = Checking("balance.txt", 5.0)
checking.deposit(25.00)
print(account.balance)
checking.transfer(125.00)
print(checking.balance)
checking.commit()
print(checking.balance)