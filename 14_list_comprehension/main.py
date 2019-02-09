#!/usr/bin/env python3

# Example 1
Celcius = [39.2, 36.5]
Fahrenheit = [ ((float(9)/5) * x + 32) for x in Celcius ]
print(Fahrenheit) # [102.56, 97.7]

# Example 2
oneToFive = [(x) for x in range(1, 6)]
print(oneToFive) # [1, 2, 3, 4, 5]

# Example 3
# usual, non pythonic way
oneList = []
for x in range(1, 30):
    for y in range(x, 30):
        for z in range(y, 30):
            if x**2 + y**2 == z**2:
                #print("(%d, %d, %d), " % (x, y, z))
                aTuple = (x, y, z)
                oneList.append(aTuple)
print(oneList)

# now see how it would be if we use list comprehension
thisList = [ (x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z **2 ]
print(thisList)
# result: [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26), (12, 16, 20), (15, 20, 25), (20, 21, 29)]


# Example 4
# A×B = {(a, b) : a belongs to A, b belongs to B}
colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]

# Usual, non pythonic way
usualList = []
for c in colours:
    for t in things:
        usualList.append((c, t))
print(usualList)

# with list comprehension:
coolList = [(c, t) for c in colours for t in things]
print(coolList)

# result: [('red', 'house'), ('red', 'car'), ('red', 'tree'), ('green', 'house'), ('green', 'car'), ('green', 'tree'), ('yellow', 'house'), ('yellow', 'car'), ('yellow', 'tree'), ('blue', 'house'), ('blue', 'car'), ('blue', 'tree')]