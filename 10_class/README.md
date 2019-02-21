# Inheritance in Python
https://www.python-course.eu/python3_inheritance.php

Example:
```python
class Person:
    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age
    
    # this __str__ is like toString in Java
    def __str__(self):
        return self.firstname + " " + self.lastname

class Employee(Person):
    def __init__(self, first, last, age, staffnum):
        super().__init__(first, last, age)
        self.staffnumber = staffnum
    
    def __str__(self):
        return super().__str__() + ", " + self.staffnumber

x = Person("Adika Bintang", "Sulaeman", 24)
y = Employee("Eric", "Johnson", 28, "123")
print(x) # will call the Person.__str__
print(y) # will call the Employee.__str__
```

## Polymorphism in Python with Abstract Class
Example:
```python
class Document:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        raise NotImplementedError("Subclass must be implement abstract method")

class Pdf(Document):
    def show(self):
        return "Show pdf contents!"
    
class Word(Document):
    def show(self):
        return "Show word documents!"

documents = [Pdf("a.pdf"), Word("b.doc")]
for d in documents:
    print(document.name + ": " + document.show())
```