import random
def new_hat():
    hat = [c for c in ['black', 'red', 'blue'] \
             for i in range(4)]
    random.shuffle(hat)  # 打乱顺序
    return hat

n, N = 5, 10000  # 一次摸 n 个球, 独立实验 N 次
M = 0
for e in range(N):
    balls = new_hat()[0:n]
    if balls.count('black') >= 2:
        M += 1
print('概率：', M/N)
