# Python Decorator
Tutorial: https://realpython.com/primer-on-python-decorators/ 

Syntax:
```python
@login_required # this is the decorator
def get_data():
    return something
```

Decorators wrap a function, modifying its behavior.

## @property decorator
Tutorial: https://www.python-course.eu/python3_properties.php

Take a look at these examples:

Example 1:
```python
class P:
    def __init__(self, x):
        self.x = x

    def set_x(self, x):
        if x > 100:
            raise ValueError("no more than 100")
        self.x = x

jir = P
jir.x = 101 # shieeettt we don't allow x > 100 but we didn't set it with set_x
# aaaand Python does not have private value
```

Then, how?

Example 2:
```python
class P:
    def __init__(self, x):
        self.x = x
    
    @property
    def x(self): # 1. see this x
        return self.__x

    @x.setter ## 2. see this corresponding x from number 1
    def set_x(self, x):
        if x > 100:
            self.__x = 0
            raise ValueError("no more than 100")
        self.__x = x

p1 = P(101) # will throw an exception
print(p1.x) # output: 0

p2 = P(2)
p2.x = 103 # will throw an exception
```