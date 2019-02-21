# https://realpython.com/primer-on-python-decorators/ 

def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@my_decorator
def say_sth():
    print("Kancut!")

say_sth()
print("now you have something in mind about @login_required of Django")
