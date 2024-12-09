import numpy as np; import matplotlib.pyplot as plt
def f(x, s, m=0):
    return 1/(2*np.pi)**0.5/s * np.exp(-1/2*((x-m)/s)**2)

S = np.linspace(2, 0.2, 31)
x = np.linspace(-5, 5, 1000)

lines = plt.plot(x, f(x,2))
plt.axis([-5, 5, -0.1, 2.1])
for i, s in enumerate(S):
    lines[0].set_ydata(f(x,s)) # set_data(x, f(x,s))
    plt.legend(['s = %4.2f' % s])
    plt.savefig('tmp_%04d.png' % i)
    plt.pause(0.1)
