# List Comprehension
tutorial: https://www.python-course.eu/python3_list_comprehension.php

## What it is
List comprehension can be used as *elegant way* to define and create list in Python. It can also be used to substitute the lambda and map function as in lesson 13: lambda and map.

## Examples
As in lesson 13: lambda and map, we can do the same here with list comprehension.
```python
Celcius = [39.2, 36.5]
Fahrenheit = [ ((float(9)/5) * x + 32) for x in Celcius ]
print(Fahrenheit)
# result: [102.56, 97.700000000000000003]
```
