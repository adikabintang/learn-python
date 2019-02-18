tutorial: https://docs.python.org/3/tutorial/errors.html

Example:
```python
import sys

try:
    f = open('file.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer")
except: # note 1
    print("unexpected error:", sys.exc_info()[0])
    raise # note 2
else: # note 3
    print("file.txt has ", len(f.readlines()), " lines")
    f.close()
```

`# note 1`: wildcard exception. triggered when none of the above exceptions catches the error.

`# note 2`: like `throw` in C++/Java

`# note 3`: it's run when the try clause does not raise an exception.