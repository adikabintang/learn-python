import numpy as np

# "rank" is the number of dimensions of the array
a = np.array([1, 2, 3]) # this is a rank 1 array
print(type(a))

# the "shape" of the array: tuple of integers giving the size of the array
# along each dimension
print("shape")
print(a.shape) # (3,)

print("val")
print(a[0], a[1], a[2])
a[0] = 5
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]]) # this is a rank 2 array
print("shape")
print(b.shape) # (2, 3)
print(b)
print(b[0, 0]) # 1
print(b[0, 2]) # 3
print(b[1, 2]) # 6

c = np.zeros((2, 2)) # for 0s, np.ones for 1s
# [[0. 0.]
#  [0. 0.]]
print(c)

# for constant array
d = np.full((2, 2), 7)
print(d)

# create an identity matrix I (capital letter i, that's why it is np.eye)
e = np.eye(2)
# [[1. 0.]
#  [0. 1.]]
print(e)

# create an array filled with random values
f = np.random.random((2, 2))
print(f)