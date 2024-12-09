import random, matplotlib.pyplot as plt
N = 500
r = [random.uniform(-1,1) for i in range(N)]
plt.plot(r, 'o')
plt.show()
