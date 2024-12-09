import random, numpy as np

def MCpi(N):
    n = 0
    for i in range(N):
        x = random.random()
        y = random.random()
        if x**2+y**2<1:
            n += 1
    return 4*n/N

def MCpi_vec(N):
    x = np.random.rand(N)
    y = np.random.rand(N)
    r = x**2 + y**2
    return 4*np.sum(r<1)/N

def MCpi2(Nmax, n):
    pi_values, N_values = [], []
    Nin = 0
    for N in range(1, Nmax+1):
        x = random.random()
        y = random.random()
        if x**2+y**2<1:
            Nin += 1
        if N % n == 0:
            pi_values.append(4*Nin/N)
            N_values.append(N)
    return N_values, pi_values

if __name__=='__main__':
    Nmax = 1000000
    print('pi_MC =', MCpi(Nmax))
    print('pi_MC_vec =', MCpi_vec(Nmax))

    import matplotlib.pyplot as plt
    N, pi = MCpi2(Nmax, int(Nmax/1000))
    error = np.abs(np.pi - np.array(pi))
    plt.plot(N, error,'-')
    plt.show()
