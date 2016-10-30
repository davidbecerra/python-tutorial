import numpy as np


# Create vectors
v1 = np.array([1,2])
v2 = np.array([0,5])


# Vector arithmetic
v1 + v2
v1 * v2  # element-wise product
np.dot(v1, v2)  # dot product
2.0 * v1


print "v1 = " + repr(v1)
print "v2 = " + repr(v2)
print "v1 + v2 = " + repr(v1 + v2)
print "v1 * v2 = " + repr(v1 * v2)  # element-wise product
print "v1 dot v2 = " + repr(np.dot(v1, v2))  # dot product
print "2 * v1 = " + repr(2.0 * v1)
