class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    # Doc

    """Doc of checking class goes here"""

    # Type

    type = "checking"

    # Constructor

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    # Method
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


# instance of checking class
checking = Checking("balance.txt", 1)
# checking.deposit(10)
checking.transfer(100)
checking.commit()
print(checking.balance)

print(checking.type)
print(checking.__doc__)

# account = Account("balance.txt")
# print(account.balance)
# account.deposit(200)
# print(account.balance)
# account.commit()
