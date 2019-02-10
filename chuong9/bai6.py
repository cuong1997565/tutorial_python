# any, all function 
# number1 = [2,4,6,8,10]
# number2 = [1,2,3,4,5,6]

# print all([num % 2 == 0 for num in number1 ])
# print any([num % 2 != 0 for num in number2])
# evens1 = []
# for num in number1:
#     if num % 2 == 0:
#         evens1.append(num)
# print all([True, True, True,True,True])

def my_sum(*args):
    total = 0
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        for num in args:
            total += num
        return total
    else:
        return "Worning input"
print my_sum(1,2,3,4,5,8.9,'dasd')