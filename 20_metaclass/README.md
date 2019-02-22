# metaclass
https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python

https://www.python-course.eu/python3_metaclasses.php 

- A metaclass is the class of a class. Think about it: class defines how an *instance* of the class behaves, a metaclass defines how a *class* behaves. *A class is an instance of a metaclass*.
- A metaclass is most commonly used as a *class-factory* (note: *not object-factory*). 
- Metaclasses allow us to do 'extra things' when creating a class, like registering the new class with some registry, or replace the class with something else entirely.
- 