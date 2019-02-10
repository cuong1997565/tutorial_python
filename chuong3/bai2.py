# def is_palindrom(word):
#     reversed_word = word[::-1]
#     print reversed_word
#     if word == reversed_word:
#         return True
#     else:
#         return False
# is_palindrom("naman")
# print is_palindrom("horse")

# fibonacci
# def fibonacci_seq(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print a
#     elif n == 2:
#         print(a,b)
#     else:
#         print(a,b)
#         for i in range(n-2):
#             c = a + b
#             a = b
#             b = c
#             print b
# fibonacci_seq(10)

# def user_info(first_name, last_name, age):
#     print "Your first name is ", first_name
#     print "Your last name is ", last_name
#     print "Your age is ", age
# user_info('Harshit', 'Vashist', 24)


#scope
x = 5 # global variables
def func():
    global x
    x = 9 # local variables
    return x
print x
print func()
print x
