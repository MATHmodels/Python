class Line:
    def __init__(self, c0, c1):
        self.c0, self.c1 = c0, c1
    def __call__(self, x):
        return self.c0 + self.c1*x
    def table(self, L, R, n): # 返回 L，R 之间 n 个点的表格
        s = '%4s %4s\n' % ('x', 'y')
        import numpy as np
        for x in np.linspace(L, R, n):
            s += '%4g %4g\n' % (x, self(x))
        return s
if __name__=='__main__':
    L = Line(1, -2)
    print('y(2) =', L(2))
    print(L.table(0, 1, 3))
