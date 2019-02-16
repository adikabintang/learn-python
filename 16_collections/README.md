# Named Tuples
source: https://stackoverflow.com/questions/2970608/what-are-named-tuples-in-python

Named tuple instances can be referenced using object-like variable dereferencing or the standard tuple syntax. They can be used similarly to `struct` but it's immutable.

## Example of tuple without named tuple
`(x, y)` tuple represents a point.

```python
point_1 = (1.0, 5.0)
point_2 = (2.5, 1.5)

from math import sqrt
line_length = sqrt( (point_1[0] - point_2[0])**2 +  (point_1[1] - point_2[1])**2)
```

## Example with named tuple
It becomes more readable.
```python
from collections import namedtuple

Point = namedtuple('Point', 'x y')
pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

from math import namedtuple
line_length = sqrt((pt1.x - pt2.x)**2 + (pt1.y - pt2.y)**2)
```

Yet another example of named tuple from Hackerrank ([link](https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?h_r=next-challenge&h_v=zen)).

```python
from collections import namedtuple
Car = namedtuple('Car', 'Price Mileage Color Class')
xyz = Car(Price = 1000, Mileage = 30, Color = 'Blue', Class = 'Y')
print(xyz) # output: Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print(xyz.Color) # output: Blue
```

We should use named tuples instead of tuples anywhere we think object notation will make the code more pythonic and more easily readable.