import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 3, 51)
y = t**2*np.exp(-t**2)

plt.plot(t, y)

# 可保成图像为指定格式
plt.savefig('fig.pdf')
plt.savefig('fig.png')
plt.savefig('fig.eps')

plt.show()
