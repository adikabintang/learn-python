import numpy as np

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

# elementwise sum, both ways are actually the same
# [[ 6.  8.]
#  [10. 12.]]
print(x + y) # also doable: x-y, x * y, x / y
print(np.add(x, y)) # subtract, multiply, divide, sqrt

# x * y is elementwise multiplication, not matrix multiplication
# use np.dot() to compute product of vectors, multiply a vector by matrix
# and to multiply matrices

v = np.array([9, 10])
w = np.array([11, 12])

# these two are the same
print(v.dot(w))
print(np.dot(v, w))

# sum
print(np.sum(x)) # 10.0
print(np.sum(x, axis=0)) # [4. 6.]
print(np.sum(x, axis=1)) # [3. 7.]

print(x)
# [[1. 2.]
#  [3. 4.]]

# transpose
# [[1. 3.]
#  [2. 4.]]
print(x.T)