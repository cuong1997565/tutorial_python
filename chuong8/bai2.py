# def total(a,b):
#     return a+b
# print total(3,10,3)

# args
# def all_total(*nums):
#     total = 0
#     for num in nums:
#        total += num
#     return total
# print all_total(1,2,3,4,5,6)

# *args with normal parameter
# def multiply_nums(num,*args):
#     multiply = 1
#     print num
#     print args
#     for i in args:
#         multiply *= i
#     return multiply
# print multiply_nums(2,2,4)

def multiply_nums(*args):
    multiply = 1
    print args
    for i in args:
        multiply *= i
    return multiply
nums = [2,3,4]
print multiply_nums(*nums)