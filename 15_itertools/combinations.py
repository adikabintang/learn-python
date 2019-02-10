#!/usr/bin/env python3

# taken from here: https://medium.com/@jasonrigden/a-guide-to-python-itertools-82e5a306cdf8
import itertools
import operator

# Example 1
shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations(shapes, 2)
for x in result:
    print(x)
# result:
# ('circle', 'triangle')
# ('circle', 'square')
# ('triangle', 'square')

print()
three_combinations = itertools.combinations(shapes, 3)
for x in three_combinations:
    print(x)
# result:
# ('circle', 'triangle', 'square')

# Example 2: combinations_with_replacement()
print()
result_w_rep = itertools.combinations_with_replacement(shapes, 2)
for x in result_w_rep:
    print(x)
# result:
# ('circle', 'circle')
# ('circle', 'triangle')
# ('circle', 'square')
# ('triangle', 'triangle')
# ('triangle', 'square')
# ('square', 'square')