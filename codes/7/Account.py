class Account:
    def __init__(self, name, account_number, init_amount):
        self.name = name
        self.no = account_number
        self.balance = init_amount
    def deposit(self, amount):  self.balance += amount
    def withdraw(self, amount): self.balance -= amount
    def dump(self):
        print('%s, %s, balance: %s' %\
        (self.name, self.no, self.balance))

if __name__=='__main__':
    a1 = Account('Zhang san', '199407292637', 20000)
    a2 = Account('Li si', '198706093029', 20000)
    a1.deposit(1000)
    a1.withdraw(4000)
    a2.withdraw(10500)
    a1.withdraw(3500)
    print("a1's balance:", a1.balance)
    a1.dump()
    a2.dump()
