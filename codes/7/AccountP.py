class AccountP:
    def __init__(self, name, account_number, init_amount):
        self.__name = name
        self.__no = account_number
        self.__balance = init_amount
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def get_balance(self): # 获取余额
        return self.__balance
    def dump(self):
        print('%s, %s, balance: %s' % \
            (self.__name, self.__no, self.__balance))

if __name__=='__main__':
    a1 = AccountP('Zhang san', '199407292637', 20000)
    a1.withdraw(4000)
    a1.__name = 'Li si'        # 增加了一个普通属性，但不改变私有属性
    print(a1.__name)           # 此时访问的是普通属性
    print(a1._AccountP__name)  # 私有属性外部访问方式
    a1.dump()
    a1.get_balance()           # a1.__balance 会报错
