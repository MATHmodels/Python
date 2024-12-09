import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 3, 51)
y = t**2*exp(-t**2)

plt.plot(t, y, '--r', \
         label='$t^2 e^{-t^2}$')
         
plt.axis([0,3, 0,0.4])
plt.title('My First Demo')
plt.xlabel('t'); plt.ylabel('y')
plt.legend()
plt.show()
