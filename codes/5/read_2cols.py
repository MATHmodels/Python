import matplotlib.pyplot as plt
import numpy as np

# 第一种方式
x, y = [], []
infile = open('xy.dat', 'r')
for line in infile:
    coords = line.split()
    x.append(float(coords[0]))
    y.append(float(coords[1]))
infile.close()

x, y = np.array(x), np.array(y)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 第二种方式
coords = np.loadtxt('xy.dat')
x, y = coords[:,0], coords[:,1]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

