class Y:
    def __init__(self, v0): # 构造函数
        self.v0 = v0
        self.g = 9.81
    def value(self, t):
        return self.v0*t - 0.5*self.g*t**2
    
y = Y(v0=3) #创建实例（对象）
v = y.value(0.1)
print(v)

from numpy import linspace, pi, sin, exp

def table(f, tstop, n):
    print('-'*12)
    for t in linspace(0, tstop, n):
        print('%4.2f %7.2f' % (t, f(t)) )

def g(t): 
    return sin(t)*exp(-t)
    
table(g, 2*pi, 6)       # 调用普通函数

y = Y(6.5)
table(y.value, 2*pi, 6) # 调用类方法
