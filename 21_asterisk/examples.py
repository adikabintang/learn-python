"""
Common use case of *, other then multiplication
see: https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558
"""

### for initializing list type containers
zeros_list = [0] * 10 # res: [0, 0, 0, ...]
zeros_tuple = (0,) * 10 # res: (0, 0, 0, ...)
print(zeros_list)
print(zeros_tuple)

### for variadic arguments
def save_ranking(*args):
    print(args)

save_ranking('a', 'b', 'c') # res: ('a', 'b', 'c')

### variadic with keyword args
def another_save(**kwargs):
    print(kwargs)

# res: {'first': 'budjana', 'second': 'tohpati'}
another_save(first='budjana', second='tohpati')

### for unpacking the containers
from functools import reduce

def product(*numbers):
    return reduce(lambda x, y: x * y, numbers)

primes = [2, 3, 5, 7]
print(product(*primes)) # res: 210
print(product(primes)) # res: [2, 3, 5, 7]

def pre_process(**headers):
    content_length = headers['Content-Length']
    print('content length: ', content_length)
    if 'https' not in headers['Host']:
        raise ValueError("You must use SSL")

try:
    headers = {
        'Accept': 'text/plain',
        'Content-Length': 348, 
        'Host': 'http://mingrammer.com' 
    }

    pre_process(**headers)
except ValueError as err:
    print("error: ", err)
