Tutorial:
- https://medium.com/@jasonrigden/a-guide-to-python-itertools-82e5a306cdf8

# What is itertools
"The `itertools` module is a collection of tools for handling iterators".

# The Itertools Module
### accumulate()
```python
itertools.accumulate(iterable[, func])
```
`accumulate()` = _akumulasi_
`func` is functions, and that parameter is optional.
_if no func is given, then the items will be summed_

### combinations()
```python
itertools.combinations(iterable, r)
```
input: iterable and integer r
output: unique combination that have r members

### combinations_with_replacement()
```python
itertools.combinations_with_replacement(iterable, r)
```

like `combination()` function, but this one allows individual elements to be repeated more than once.