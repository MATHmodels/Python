import random, matplotlib.pyplot as plt 
m, s, N = 0, 1, 1000
r = [random.gauss(m, s) for i in range(N)]
plt.hist(r)
plt.show()
