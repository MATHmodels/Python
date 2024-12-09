import numpy as np

A = np.array([[1, 1, 1],
              [0, 2, 5],
              [2, 5, 1]])
b = np.array([6, -4, 27])

# A*x = b => x = inv(A)*b
x = np.dot(np.linalg.inv(A), b)
print('x = %g, y = %g, z = %g' %(x[0], x[1], x[2]))
