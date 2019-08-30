import numpy as np

# we will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])

# y is an empty matrix with the same shape as x
y = np.empty_like(x)

# add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v

# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print(y)

# faster alternative
# approach: create a matrix vv by stacking v vertically, then performing 
# elementwise summation of x and vv
vv = np.tile(v, (4, 1))
# [[1 0 1]
#  [1 0 1]
#  [1 0 1]
#  [1 0 1]]
print(vv)
r = x + vv # r = y

# taking fully advantage of "broadcasting", we can do x + v directly
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print(x + v)