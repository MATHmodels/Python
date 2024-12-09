import numpy as np
N = 100000
r = np.random.randint(1, 7, size=(2,N))
black, green = r[0,:], r[1,:]
M = np.sum(black > green)
print('概率: %.4f' % (M/N))
