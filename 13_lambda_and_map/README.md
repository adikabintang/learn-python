# Lambda Basic
Tutorial:
https://www.python-course.eu/python3_lambda.php

The general syntax of lambda:
```
lambda argument_list: expression
```

For example, the conventional function:
```python
def sum(x, y):
    return x + y

# call sum(x, y) function
sum(3, 4) # return 7
```

With lambda, we can write equivalent function:
```python
sum = lambda x, y: x + y

# call sum(x, y) function
sum(3, 4) # return 7
```

Lambda is handy to use with `map`. 

The goal is similar to C++'s lambda `[](){}`

# Map Basic
Tutorial:
- https://www.w3schools.com/python/ref_func_map.asp
- and the lambda tutorial website above

From w3schools:

"The `map()` function executes a specified function for each item in an interable."

Syntax:
```python
map(function, iterables)
```

Example:
```python
def fahrenheit(T):
    return ((float(9)/5) * T + 32)

temperatures = (36.5, 37, 38)
t_in_f = map(fahrenheit, temperatures)

print(list(t_in_f)) 
# output:
# [97.7, 98.6000000000001, 100.4]
```

When using lambda instead of conventional function, it would be:
```python
temperatures = (36.5, 37, 38)
t_in_f = map(lambda x: ((float(9)/5) * T + 32), temperatures)

print(list(t_in_f)) 
# output:
# [97.7, 98.6000000000001, 100.4]
```
