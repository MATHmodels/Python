class Forward1:
    def __init__(self, f, h=1E-5):
        self.f, self.h = f, h
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h
class Backward1:
    def __init__(self, f, h=1E-5):
        self.f, self.h = f, h
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h
class Central4:
    # 同样的构造函数
    # 在__call__中实现需要的公式
