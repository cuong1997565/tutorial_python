# def to_power(num, *args):
#     if args:
#         return [i**num for i in args]
#     else:
#         return "You didn't pass any args"
# nums = [1,2,3]
# print to_power(2,*nums)

#kwargs as a parameter
# def func(**kwargs):
#     for k,v in kwargs.items():
#         print k + " : "+v
# func(first_name = 'harshit', last_name = 'Vashistha')
# dictionary unpacking

# def func(name = 'unknown', age = 24):
#     print name
#     print age
# func('harshit')

# def func(name,*args, **kwargs):
#     print name
#     print args
#     # print last_name
#     print kwargs
# func('harshit',1,2,3,a=1,b=2)

##############
def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
names = ['harshit','mohit']
print func(names, reverse_str = True)
