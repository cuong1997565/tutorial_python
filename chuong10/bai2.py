# function returning function

# def outer_func():
#     def inner_func():
#         print 'inside inner func'
#     return inner_func
# var = outer_func()
# var()

# def outer_func2(msg):
#     def inner_func2():
#         print "message is ", msg
#     return inner_func2
# var = outer_func2('Hi there !')
# var()


# function returning function (closure) practice
# def to_power(x):
#     def calc_power(n):
#         return n**x
#     return calc_power
# cube = to_power(3)
# print cube(5) 

#Decorators - enhance the functionality of other functions
def decorator_function(any_function):
    def wrapper_function():
        print 'this is awesome function'
        any_function()
    return wrapper_function
#this is awesome function
@decorator_function
def func1():
    print 'this is function 1'
func1()
#this is awesome function
def func2():
    print 'this is function 2'

# func1()
# func2()
# var = decorator_function(func1)
# var()