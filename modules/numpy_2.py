import numpy as np


v1 = np.array([1,2])

# Matrices
A = np.array([[1, 2], [3, 4]])
np.matmul(A, v1)  # Apply matrix A to v1

np.linalg.solve(A, v1)  # Solve Ax = v1


print "A v1 = " + repr(np.matmul(A, v1))
print "Ax = v1 -> x = " + repr(np.linalg.solve(A, v1))