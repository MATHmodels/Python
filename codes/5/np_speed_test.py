import numpy as np; from math import sin
from timeit import timeit
x = np.linspace(0, 2*np.pi, 100001); y = np.zeros(len(x))

t1 = timeit('for i in range(len(x)): y[i] = sin(x[i])',\
            globals=globals(), number=10)
t2 = timeit('for i in range(len(x)): y[i] = np.sin(x[i])',\
            globals=globals(), number=10)
t3 = timeit('y = np.sin(x)', globals=globals(), number=10)

print('loop: %2.4f, np loop:%2.4f, np: %2.4f' % (t1,t2,t3))
