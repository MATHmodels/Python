from Integrate import Integrator
import numpy as np

class Simpson(Integrator):
    def construct_method(self):
        if self.n % 2 != 1:
            print('n=%d must be odd, 1 is added' % self.n)
            self.n += 1
        x = np.linspace(self.a, self.b, self.n)
        h = (self.b - self.a)/float(self.n - 1)*2
        w = np.zeros(len(x))
        w[0:self.n:2] = h/3
        w[1:self.n-1:2] = 2*h/3
        w[0] /= 2
        w[-1] /= 2
        return x, w

if __name__ == '__main__':
    def f(x):
        return x*x
    method = Simpson(0, 2, 101)
    print(method.integrate(f))
