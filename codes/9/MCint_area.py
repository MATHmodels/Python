import random, numpy as np
def MCint_area(f, a, b, m, N):     # 标量版本
    below = 0
    for i in range(N):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            below += 1
    return below/N*m*(b-a)

def MCint_area_vec(f, a, b, m, N): # 矢量版本
    x = np.random.uniform(a, b, N)
    y = np.random.uniform(0, m, N)
    below = np.sum(y < f(x))
    return below/N*m*(b-a)

def MCint2_area(f, a, b, m, Nmax, n=1000):
    I_values, N_values = [], []
    below = 0
    for N in range(1, Nmax+1):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            below += 1
        if N % n == 0:
            I = below/N*m*(b-a)
            I_values.append(I)
            N_values.append(N)
    return N_values, I_values

if __name__=='__main__':
    f = lambda x: 2 + 3*x
    a = 1; b = 2; Nmax = 1000000; m = f(b)
    print(MCint_area(f, a, b, m, Nmax))
    print(MCint_area_vec(f, a, b, m, Nmax))

    import matplotlib.pyplot as plt
    random.seed(2)
    n = 10000;
    N, I = MCint2_area(f, a, b, m, Nmax, n)
    print(I[-1])
    error = np.abs(6.5 - np.array(I))
    plt.plot(N, error)
    plt.show()
