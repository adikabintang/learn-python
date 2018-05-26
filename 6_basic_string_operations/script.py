#!/usr/bin/python3

str_1 = "Greg Howe Man ESP"
print(str_1.index("e"))
print(str_1.count("e"))
print(str_1[2:6])
print(str_1[2:12:2]) # [start:stop:step]
print("reverse: %s" % str_1[::-1])
print(str_1.upper())
print(str_1.lower())
print(str_1.startswith("Greg"))
print(str_1.endswith("asdfasdfasdf"))
print(str_1.split(" "))