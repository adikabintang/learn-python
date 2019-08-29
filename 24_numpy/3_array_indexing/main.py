import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

row_r1 = a[1, :]
print(row_r1) # [5 6 7 8]

row_r2 = a[1:2, :]
print(row_r2) # [[5 6 7 8]]

col_r1 = a[:, 1]
print(col_r1) # [ 2  6 10]

col_r2 = a[:, 1:2]
# [[ 2]
#  [ 6]
#  [10]]
print(col_r2)

print("---")
p = np.array([[1, 2], [3, 4], [5, 6]])

# see this pattern
# p[[0, 1, 2], [0, 1, 0]] = np.array(a[0, 0], a[1, 1], a[2, 0]) = [1 4 5]
print(p[[0, 1, 2], [0, 1, 0]])

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
print(x)

b = np.array([0, 2, 0, 1])
print(np.arange(4)) # [0 1 2 3]
print(x[np.arange(4), b]) # = x[[0, 1, 2, 3], [0, 2, 0, 1]] = [ 1  6  7 11]

x[np.arange(4), b] += 10
# [[11  2  3]
#  [ 4  5 16]
#  [17  8  9]
#  [10 21 12]]
print(x)