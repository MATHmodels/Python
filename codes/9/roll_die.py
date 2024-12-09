import random
def six_eyes(N):     # 掷N次色子，计算出现6的概率
    M = 0
    for i in range(N):
        outcome = random.randint(1, 6)
        if outcome == 6:
            M += 1
    return M/N

import numpy as np
def six_eyes_vec(N): # 掷N次色子，计算出现6的概率
    eyes = np.random.randint(1, 7, N)
    success = eyes == 6
    M = np.sum(success)
    return M/N

if __name__ == '__main__':
    N = 10000
    print(six_eyes(N))
    print(six_eyes_vec(N))



