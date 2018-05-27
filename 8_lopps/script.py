#!/usr/bin/python3

print("example 1")
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

print("example 2")
for x in range(5):
    print(x)

print("example 3")
for x in range(3, 6):
    print(x)

print("example 4")
for x in range(3, 8, 2): # (start, stop, step)
    print(x)

print("example 5")
count = 0
while count < 5:
    print(count)
    count += 1

print("example 6")
i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        break

print("example 7")
for i in range(0, 5):
    if i % 2 == 0:
        print(i)

print("example 8")
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("else after while")

print("example 9")
for i in range(1, 10):
    if i == 5:
        break
    print(i)
else:
    print("if it hits 'break', 'else' will not be executed")