# number = list(range(1,11))
# print number
# number.pop()
# print number


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def negative_list(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative
# print negative_list(numbers)

def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
numbers = list(range(1,11))
print square_list(numbers)