import numpy as np

# compute outer product of vectors
v = np.array([1, 2, 3]) # v has shape (3,)
w = np.array([4, 5]) # w has shape (2,)

# to compute an outer product, we first reshape v to be a column vector of
# shape (3, 1); we can then broadcast it against w to yield an output of
# shape (3, 2), which is the outer product of v and w

# [1 2 3]
print(v)

# [[1]
#  [2]
#  [3]]
print(np.reshape(v, (3, 1)))

# [[ 4  5]
#  [ 8 10]
#  [12 15]]
print(np.reshape(v, (3, 1)) * w)

###

# add a vector to each row of a matrix
x = np.array([[1, 2, 3], [4, 5, 6]])
# x has shape (2, 3) and v has shape (3,) so they broadcast to (2, 3)

# [[2 4 6]
#  [5 7 9]]
print(x + v)

###

# add a vector to each column of a matrix
# x has shape (2, 3) and w has shape (2,)
# the shape of transpose x = (3, 2)
# broadcast x.T against w, the result shape is (2, 3)

# [[ 5  6  7]
#  [ 9 10 11]]
print((x.T + w).T) # = x + np.reshape(w, (2, 1))

###
# multiply a matrix by a constant:
# [[ 2  4  6]
#  [ 8 10 12]]
print(x * 2)
