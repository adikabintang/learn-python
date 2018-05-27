#!/usr/bin/python3

x = 2
print(x == 2)
print(x == 3)

name = "Pat"
age = 21

if name == "John" and age == 23:
    print("Right, John")
elif name == "Pat" and age == 20:
    print("Pat is right")
else:
    print("Hee?")

print("'is' operator compares instance, not value")
p = 2
q = 3
r = p
print(p is q)
print(r is p)