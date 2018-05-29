#!/usr/bin/python3

from another_module import AnotherModule
import module_functions
from foo.bar import Bar

print("oi")
a_module = AnotherModule()
a_module.do_something()
module_functions.my_function()
a_module.member_one = "nyooo"
a_module.do_something()

a_bar = Bar()
a_bar.func()