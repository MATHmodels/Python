class MyClass:
    def __init__(self, p1, p2):
        self.attr1, self.attr2 = p1, p2
    def method1(self, arg):
        self.attr3 = arg     # 可以在构造函数外增加变量
        return self.attr1 + self.attr2 + self.attr3
    def method2(self):
        print('Hello!')

m = MyClass(4, 10)
print(m.method1(-2))
m.method2()
