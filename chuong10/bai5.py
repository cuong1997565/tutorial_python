# #exercise decorator
# import time
# t1 = time.time()
# print 'this is line one'
# x = 5
# if x == 5 :
#     print 'x is equal to 5'
# print 'this is line two'
# t2 = time.time()
# print t2-t1

from functools import wraps
import time
def calculate_time(function):
    @wraps(function)
    def calculate_time(function):
        def wrapper(*args, **kwargs):
            print 'Executing ... ',function.__name__
            t1 = time.time()
            returned_value = function(*args, **kwargs)
            t2 = time.time()
            total_time = t2 - t1
            print 'This function took ', total_time,' secound'
            return returned_value
        return wrapper

@calculate_time
def square_finder(n):
    return [i**2 for i in range(1,n+1)]

square_finder(1000)
