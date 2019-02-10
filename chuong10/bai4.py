from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print "You are calling ", function.__name__
        print function.__doc__
        return function(*args, **kwargs)
    return wrapper

@print_function_data
def add(a,b):
    return a+b
print add(4,6)