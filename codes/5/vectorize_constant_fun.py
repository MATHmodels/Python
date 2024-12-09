import numpy as np

def fs(x): return 2

def fv(x): return np.zeros(x.shape, x.dtype) + 2

def f(x):
    if isinstance(x, (float, int)): return fs(x)
    elif isinstance(x, np.ndarray): return fv(x)
    else: raise TypeError( 'x 必需数字或数组')
         
print(fs(12))
print(fv(np.array([1,2,3])))
print(f(12))
print(f(np.array([1,2,3])))

