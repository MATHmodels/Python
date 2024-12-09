import numpy as np
import matplotlib.pyplot as plt
def f(x, s, m=0):
    return 1/(2*np.pi)**0.5/s * np.exp(-1/2*((x-m)/s)**2)

S = np.linspace(2, 0.2, 31)
x = np.linspace(-5, 5, 1000)

import matplotlib.animation as animation
fig = plt.figure()
lines = plt.plot(x, f(x,2))
plt.axis([-5, 5, -0.1, 2.1])

def frame(args): # 返回动画中的一帧图像
    i, s, x, lines = args
    y = f(x, s)
    lines[0].set_data(x, y)
    return lines

args = [(i, s, x, lines) for i, s in enumerate(S)]
m = animation.FuncAnimation(fig, frame, args, interval=150)
m.save('movie.gif', fps=5)
plt.show()
