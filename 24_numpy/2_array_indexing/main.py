import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
print(a)

b = a[:2, 1:3]
# [[2 3]
#  [6 7]]
print(b)

print(a[0, 1]) # 2
b[0, 0] = 77
print(a[0, 1]) # 77

x = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(x)
y = x[:, :, 0]
print(y)