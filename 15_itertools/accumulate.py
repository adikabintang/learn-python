#!/usr/bin/env python3

# taken from here: https://medium.com/@jasonrigden/a-guide-to-python-itertools-82e5a306cdf8
import itertools
import operator

data = [1, 2, 3, 4, 5]

# Example 1
result = itertools.accumulate(data, operator.mul)
for x in result:
    print(x)
# result:
# 1       -> 1
# 2       -> 1 * 2
# 6       -> 1 * 2 * 3 
# 24      -> 1 * 2 * 3 * 4
# 120     -> 1 * 2 * 3 * 4 * 5

# Example 2
print()
second_data = [5, 2, 8, 5]
result_second = itertools.accumulate(second_data, max)
for x in result_second:
    print(x)
# result:
# 5         -> 5
# 5         -> max(5, 2) = 5
# 8         -> max(5, 8) = 8
# 8         -> max(8, 5) = 8

# Example 3
print()
third_data = [5, 2, 8, 5]
result_third = itertools.accumulate(third_data) # no func given as parameter
for x in result_third:
    print(x)
# result:
# 5   -> 5
# 7   -> 5 + 2
# 15  -> 5 + 2 + 8
# 20  -> 5 + 2 + 8 + 5