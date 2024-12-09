class SelfExplorer: # Class for computing a*x
    def __init__(self, a):
        self.a = a
        print('i: id(self)=%d' % id(self))
    def value(self, x):
        print('v: id(self)=%d' % id(self))
        return(self.a*x)


s1 = SelfExplorer(1)
print(id(s1))
s1.value(4)
SelfExplorer.value(s1,4)

s2 = SelfExplorer(2)
print(id(s2))
