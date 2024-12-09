import numpy as np; from timeit import timeit

def H(x): 
    return (0 if x < 0 else 1)

def H_loop(x):           # 当 len(x) 很大时，会很慢
    r = np.zeros_like(x, dtype=int)
    for i in range(len(x)): 
        r[i] = H(x[i])
    return r

H_vec1 = np.vectorize(H) # 当 len(x) 很大时，也很慢

def H_vec2(x): 
    return np.where(x < 0, 0.0, 1.0)

x = np.linspace(-100, 100, 201)
t1 = timeit('y = H_loop(x)', globals=globals(), number=100)
t2 = timeit('y = H_vec1(x)', globals=globals(), number=100)
t3 = timeit('y = H_vec2(x)', globals=globals(), number=100)
print('loop: %2.4f, vec1: %2.4f, vec2: %2.4f' % (t1,t2,t3))
