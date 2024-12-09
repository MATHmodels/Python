import random, numpy as np
def MCint(f, a, b, n):
    s = 0
    for i in range(n):
        x = random.uniform(a, b)
        s += f(x)
    return (b-a)*s/n
def MCint_vec(f, a, b, n):
    x = np.random.uniform(a, b, n)
    s = np.sum(f(x))
    return (b-a)*s/n

if __name__=='__main__':
    f = lambda x: 1 + 2*x
    a = 1; b = 2; n = 10000
    I = MCint(f, a, b, n)
    print(I)
    I = MCint_vec(f, a, b, n)
    print(I)


