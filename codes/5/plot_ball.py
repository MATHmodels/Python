import numpy as np
import matplotlib.pyplot as plt

def yfun(v0, t, g=9.8):
    return v0*t - 1/2*g*t**2

g = 9.8
for v0 in [10, 12]:
    t = np.linspace(0, 2*v0/g, 100)
    y = yfun(v0, t, g)
    plt.plot(t, y, label='$v_0 = %.2f$ m/s' % v0)

plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.axis([0, 2.5, 0, 8])
plt.legend()
plt.savefig('plot_ball.pdf')
plt.show()
