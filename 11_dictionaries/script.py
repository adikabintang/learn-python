#!/usr/bin/python3

# Dictionary: a data structure with key value

phonebook = {
    "John": 123,
    "Frusciante": 345,
    "Jack" : 938377264,
}

print("John's: %d" % phonebook["John"])
phonebook["John"] = 890
print("John's: %d" % phonebook["John"])
del phonebook["John"]
print(phonebook)

for name, number in phonebook.items():
    print("name: %s, phone number: %d" % (name, number))