# def add_two(a,b) :
#     return a + b
# a = int(input("enter first number :"))
# b = int(input("enter second number :"))
# total = add_two(a,b)
# print(total)

# functions practice 
# def last_char(name):
#     return name[-1]
# print last_char("harship")

# def odd_even(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# a = int(input("enter one :"))
# print odd_even(a) 

def greater(a,b):
    if a > b :
        return a
    else:
        return b
# num1 = int(input("enter first number"))
# num2 = int(input("enter secound number"))
# bigger = greater(num1,num2)
# print bigger, "is greater "

# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger, c)
print new_greatest(10,30,20)

