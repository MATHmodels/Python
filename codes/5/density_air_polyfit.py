import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('density_water.dat')
T, D = data[:,0], data[:,1]

a = np.polyfit(T, D, 2)
Ti = np.arange(100)
Di = np.polyval(a, Ti)

plt.plot(T,D,'o', Ti, Di,'-')
plt.xlabel('Temperature (C)')
plt.ylabel('Density (kg/m^3)')
plt.show()
