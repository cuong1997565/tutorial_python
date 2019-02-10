# def add(a,b):
#     return a+b

# add2 = lambda a,b : a + b
# print add2(2,3)

# multiply = lambda a,b : a * b
# print multiply(2,3)

# iseven2 = lambda a : a%2==0
# print iseven2(5)

# last_char = lambda s : s[-1]
# print last_char('harshit')

#lambda with if,else 
# def func(s):
#     if len(s) > 5:
#         return True
#     return False
# func = lambda s : True if len(s) > 5 else False
# print func('abcedf')

## How we can do this without enumerate function
# names = ['abc','abcdef','harshit']
# pos = 0
# for name in names:
#     print pos , name
#     pos += 1

#########
#Define a function that take two arguments
names = ['abc','abcdef','harshit']
def find_pos(l, target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
    return -1
print find_pos(names,'harshit')