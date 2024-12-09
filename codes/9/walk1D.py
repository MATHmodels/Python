import random, numpy as np
import matplotlib.pyplot as plt
Np = 4     # 粒子数
Ns = 100   # 步数
x = np.zeros((Ns, Np))
t = np.arange(Ns)
for i in t[1:]:
    for p in range(Np):
        if random.random()<0.5:
            x[i,p] = x[i-1,p] + 1
        else:
            x[i,p] = x[i-1,p] - 1
plt.plot(x, t, '-o')
plt.show()

'''
# 运行以下代码将 Np 改大点，例如 Np = 1000
x = x[-1,:]
mean_pos = np.mean(x) # 平均位置
stdev_pos = np.std(x) # 集群宽度

plt.hist(x)           # 位置分布
plt.show()
'''
