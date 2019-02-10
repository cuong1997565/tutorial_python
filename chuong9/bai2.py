#map function 
numbers = [1,2,3,4]
def squares(a):
    return a**2
print map(lambda a:a**2, numbers)

# list comp
square_new = [i**2 for i in numbers]
print square_new

# new_list = []
# for num in numbers:
#     new_list.append(squares(num))
# print new_list

names = ['abc','abcd','abcde']
lenght = map(len, names)

for i in lenght:
    print i
for j in lenght:
    print j