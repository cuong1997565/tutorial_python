from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        print 'this is awesome function'
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def func(a):
    print 'this is function with argument', a
func(7)

@decorator_function
def add(a,b):
    return a + b
print add(2,3)
print add.__doc__
print add.__name__