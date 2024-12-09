class Y:
    def __init__(self, v0):
        self.v0, self.g = v0, 9.81
    def __call__(self, t): # def value(self, t):
        return self.v0*t - 0.5*self.g*t**2
    def __str__(self):
        return 'v0*t - 0.5*g*t**2; v0=%g' % self.v0

if __name__=='__main__':
    y = Y(3)
    v = y(0.1)  # v = y.__call__(0.1) 或
                # v = Y.__call__(y, 0.1)
    print(v)
    print(y)
