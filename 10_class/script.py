#!/usr/bin/python3

class MyClass:
    member_one = "weleh"

    # self refers to the newly created object
    # may be it is the same with 'this' keyword in C++ or Java
    def function_one(self):
        print("a message: %s" % self.member_one)

myobjectx = MyClass()
print("member_one: %s" % myobjectx.member_one)
myobjectx.function_one()