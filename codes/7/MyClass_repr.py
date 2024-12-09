class MyClass:
    def __init__(self, a, b):
        self.a, self.b = a, b
    def __str__(self):
        return 'a=%s, b=%s' % (self.a, self.b)
    def __repr__(self):
        return 'MyClass(%s, %s)' % (self.a, self.b)

if __name__=='__main__':
    m = MyClass(1, 5)
    print(m)
    print(str(m))
    s = repr(m)
    print(s)
    m2 = eval(s) #同 m2 = MyClass(1, 5)
    print(m2)
