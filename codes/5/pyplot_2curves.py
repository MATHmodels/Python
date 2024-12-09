import numpy as np
import matplotlib.pyplot as plt

f = lambda t: t**2*np.exp(-t**2)
h = lambda t: t**4*np.exp(-t**2)
t = np.linspace(0, 3, 51)

plt.plot(t, f(t), 'b-', \
         label='$t^2 e^{-t^2}$')
plt.plot(t, h(t), 'ro', \
         label='$t^4 e^{-t^2}$')
plt.axis([0,3,0,0.8])
plt.title('2 curves in 1 plot')
plt.xlabel('t'); plt.ylabel('y')
plt.legend(); plt.show()
