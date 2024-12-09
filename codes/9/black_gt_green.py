import random
N = 100000
M = 0 
for i in range(N):
    black = random.randint(1, 6)
    green = random.randint(1, 6)
    if black > green:
        M += 1
print('概率: %.4f' % (M/N))

