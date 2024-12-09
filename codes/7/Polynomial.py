class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s

    def __add__(self, other): # Return self + other
        # Start with the longest list and add in the other
        if len(self.coeff) > len(other.coeff):
            coeff = self.coeff[:]  # copy!
            for i in range(len(other.coeff)):
                coeff[i] += other.coeff[i]
        else:
            coeff = other.coeff[:] # copy!
            for i in range(len(self.coeff)):
                coeff[i] += self.coeff[i]
        return Polynomial(coeff)

    def __mul__(self, other):
        M = len(self.coeff) - 1
        N = len(other.coeff) - 1
        coeff = [0]*(M+N+1)
        for i in range(0, M+1):
            for j in range(0, N+1):
                coeff[i+j] += self.coeff[i]*other.coeff[j]
        return Polynomial(coeff)

    def differentiate(self): # change self
        for i in range(1, len(self.coeff)):
            self.coeff[i-1] = i*self.coeff[i]
        del self.coeff[-1]
    def derivative(self):    # return new polynomial
        dpdx = Polynomial(self.coeff[:])  # copy
        dpdx.differentiate()
        return dpdx

    def __str__(self):
        s = ' '
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += '+ %g*x^%d ' % (self.coeff[i], i)
        # fix layout (lots of special cases):
        s = s.replace('+ -', '- ')
        s = s.replace('x^0', '1')
        s = s.replace(' 1*', ' ')
        s = s.replace('x^1 ', 'x ')
        if s[0:3] == ' + ':  s = s[3:]
        if s[0:3] == ' - ':  s = '-' + s[3:]
        return s

    def simplestr(self):
        s = ''
        for i in range(0, len(self.coeff)):
            s += ' + %g*x^%d' % (self.coeff[i], i)
        return s

def test_Polynomial():
    p1 = Polynomial([1, -1])
    p2 = Polynomial([0, 1, 0, 0, -6, -1])
    p3 = p1 + p2
    p3_exact = Polynomial([1, 0, 0, 0, -6, -1])
    msg = 'p1 = %s, p2 = %s\np3=p1+p2 = %s\nbut wrong p3 = %s'%\
          (p1, p2, p3_exact, p3)
    assert p3.coeff == p3_exact.coeff, msg
    # Note __add__ applies lists only, here with integers, so
    # == for comparing lists is not subject to round-off errors

    p4 = p1*p2
    # p4.coeff becomes a numpy array, see __mul__
    p4_exact = Polynomial([0,  1, -1,  0, -6,  5,  1])
    msg = 'p1 = %s, p2 = %s\np4=p1*p2 = %s\ngot wrong p4 = %s'%\
          (p1, p2, p4_exact, p4)
    assert p4.coeff == p4_exact.coeff, msg

    p5 = p2.derivative()
    p5_exact = Polynomial([1, 0, 0, -24, -5])
    msg = 'p2 = %s\np5 = p2.derivative() = %s\ngot wrong p5 = %s'%\
          (p2, p5_exact, p5)
    assert p5.coeff == p5_exact.coeff, msg

    p6 = Polynomial([0, 1, 0, 0, -6, -1])  # p2
    p6.differentiate()
    p6_exact = p5_exact
    msg = 'p6 = %s\p6.differentiate() = %s\ngot wrong p6 = %s'%\
          (p2, p6_exact, p6)
    assert p6.coeff == p6_exact.coeff, msg

test_Polynomial()

if __name__ == '__main__':
    p1 = Polynomial([1, -1])
    print(p1)
    p2 = Polynomial([0, 1, 0, 0, -6, -1])
    print(p2)
    p3 = p1 + p2
    print(p3.coeff)
    print(p3)
    p2.differentiate()
    print(p2)
