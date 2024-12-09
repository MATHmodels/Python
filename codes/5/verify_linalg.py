from numpy.random import rand as rand
from numpy.linalg import det as det
import numpy as np

n = 4
A = rand(n,n)
B = rand(n,n)
C = rand(n,n)

err1 = np.abs( np.dot(A+B,C) - (np.dot(A,C) + np.dot(B,C)) )
print('max |(A+B)C - (AC+BC)| =', np.max(err1))

err2 = np.abs( np.dot(np.dot(A,B),C) - np.dot(A,np.dot(B,C)) )
print('max |(AB)C - A(BC)| =', np.max(err2))

err3 = np.abs( det(np.dot(A,B)) - det(A)*det(B))
print('max |det(AB) - det(A)det(B)| =', err3)
