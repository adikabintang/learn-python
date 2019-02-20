Zip returns a list of tuples. Just see these examples:

From https://www.hackerrank.com/challenges/zipped/problem
```python
the_array = [1, 2, 3, 4, 5]
the_string = "abcde"
print(zip(the_array, the_string))
# output:
# [(1, a), (2, b), (3, c), (4, d), (5, e)]
```

It follows the smallest length:
```python
print(zip([1, 2, 3], [6, 7, 8, 9, 0]))
# output:
# [(1, 6), (2, 7), (3, 8)]
```