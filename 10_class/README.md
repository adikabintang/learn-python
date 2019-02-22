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
# Abstract Base Class
https://www.python-course.eu/python3_abstract_classes.php 

To see a little bit about "metaclass", refer to chapter "20_metaclass".

Abstract class is a base class which the function cannot be initiated by the base because it lets the child class to implement it. 

Abstract classes are classes that contain one or more abstract methods. Abstract method is a method that is declared but does not have implementation.

Abstract classes may not be instantiated, and it requires subclasses to provide implementations.

A class that is derived from an abstract class cannot be instantiated unless all of its abstract methods are overridden.

Abstract class in C++:
```cpp
// an abstract class
class Base
{
public:
    // pure virtual function
    virtual void show() = 0;
};

class Child: public Base
{
public:
    void show() {
        std::cout << "hi" << std::endl;
    }
};
```

Python has abc: abstract base class.
```python
from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    @abstractmethod
    def do(self):
        print("do sth") # if we don't want to do anything, use "pass"

class AnotherSubclass(AbstractClassExample):
    def do(self):
        super().do() # it does not have to, especially if do super().do() is "pass"
        print("should I call you MISTAH?")

x = AnotherSubclass()
x.do()
# output:
# do sth
# should I call you MISTAH?
```