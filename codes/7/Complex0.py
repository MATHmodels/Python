class Complex:
    def __init__(self, real, imag=0.0):
        self.real, self.imag = real, imag
    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)
    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)
    def __mul__(self, other):
        real = self.real*other.real - self.imag*other.imag
        imag = self.imag*other.real + self.real*other.imag
        return Complex(real, imag)
    
    def __truediv__(self, other):
        ar, ai = self.real, self.imag
        br, bi = other.real, other.imag
        r = float(br**2 + bi**2)
        return Complex((ar*br+ai*bi)/r, (ai*br-ar*bi)/r)
    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)
    def __neg__(self):   # defines -c (c is Complex)
        return Complex(-self.real, -self.imag)
    def __eq__(self, other):
        return self.real == other.real and \
               self.imag == other.imag
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return '(%g, %g)' % (self.real, self.imag)
    def __repr__(self):
        return 'Complex' + str(self)
    
    def __pow__(self, power):
        raise NotImplementedError\
        ('power operation is not yet impl. for Complex')
    
    def __gt__(self, other):  self._illegal('>')
    def __ge__(self, other):  self._illegal('>=')
    def __lt__(self, other):  self._illegal('<')
    def __le__(self, other):  self._illegal('<=')

if __name__=='__main__':
    u = Complex(2,-1)
    v = Complex(1) # zero imaginary part
    w = u + v
    print(w)
    print(w != u)
    print(u*v)
    print(4+w)
    print(w+4)
    print(w-4)
    print(4-w)
    print(u/v)
