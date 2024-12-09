import random, numpy as np
def random_walk_2D(Np, Ns):
    x, y = np.zeros(Np), np.zeros(Np)
    for step in range(Ns):
        for i in range(Np):
            direction = random.randint(1, 4)
            if   direction == 1: y[i] += 1 # 上
            elif direction == 2: y[i] -= 1 # 下
            elif direction == 3: x[i] += 1 # 右
            elif direction == 4: x[i] -= 1 # 左
    return x, y

def random_walk_2D_vec(Np, Ns):
    x, y = np.zeros(Np), np.zeros(Np)
    moves = np.random.randint(1, 5, size=(Ns, Np))
    for step in range(Ns):
        this_move = moves[step,:]
        y += np.where(this_move==1, 1, 0) # 上
        y -= np.where(this_move==2, 1, 0) # 下
        x += np.where(this_move==3, 1, 0) # 右
        x -= np.where(this_move==4, 1, 0) # 左
    return x, y

import matplotlib.pyplot as plt
x, y = random_walk_2D_vec(1000, 100)
plt.plot(x,y,'x')
plt.show()
