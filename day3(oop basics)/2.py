class Bankacount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
    def withraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withrawn:", amount)
        else:
            print("Insufficient balance") # till now, we have just created the blueprint of the command


bcc = Bankacount("Durjoy", 5000)   # from now on, the object behaves according to the class
bcc.deposit(2000)
bcc.withraw(3000)

print("Balance:", bcc.balance)
