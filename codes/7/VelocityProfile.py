class VelocityProfile:
    def __init__(self, b, u0, n, R):
        self.b, self.u0, self.n, self.R = b, u0, n, R
    def value(self, r):
        b, u0, n, R = self.b, self.u0, self.n, self.R
        v = (b/(2*u0))**(1/n)*(n/(n+1))*\
            (R**(1+1/n) - r**(1+1/n))
        return v
        
v = VelocityProfile(0.06, 0.02, 0.1, 1)
print('%.2f' % v.value(r=0.1))
