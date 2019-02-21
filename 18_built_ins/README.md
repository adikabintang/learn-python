# zip
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

# eval
Evaluating expressions.

Example:
```python
eval("print(2 + 3")) # output: 5
eval("9 + 5") # output 14
x = 2
eval("x + 2") # output 4
```

# any
`any()` returns True if any of the elements in the iterable is true.

Example:
```python
any([1>0, 1==0, 1<0]) # output: true
any([1<0,2<1,3<2]) # output: false
```

# all
returns true if ALL of the elements are true. if the iterable is empty, it also returns True.

Example:
```python
all(['a'<'b','b'<'c']) # output: True
```

# My hackerank answer
Task:

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

```python
s = [1, 2, 3, 4, 5, -9]
print(all([int(i) > 0 for i in s]) and any([str(i) == str(i)[::-1] for i in s]))
```

That just shows the way to reverse a string in python:
```python
s = "budjana"
print(s[::-1]) # output: anajdub
```
