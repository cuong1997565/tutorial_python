#create a list of squares from 1 to 10
# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print squares

# square2 = [i **2 for i in range(1,11)]
# print square2

# names = ['Harshit','Mohit','Rohit']
# new_list = []
# for name in names:
#     new_list.append(name[0])
# print new_list

def reverse_strings(l):
    return [name[::-1] for name in l]
print reverse_strings(['abc','tuv','xyz'])

def reverse_str(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
    return new_list
print reverse_str(['abc','tuv','xyz'])