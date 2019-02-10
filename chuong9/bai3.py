#filter function 
# def is_even(a):
#     return a%2 == 0
# numbers = [3,4,2,1,5,6,9,8,10]
# evens = tuple(filter(lambda a:a%2==0,numbers))
# print evens
# new_events = [i for i in numbers if i%2==0]
# print new_events

#iterator vs iterables
numbers = [1,2,3,4] # iterables
squares = map(lambda a:a**2, numbers) #iterator
number_iter = iter(squares)
print next(number_iter)
print next(number_iter)
print next(number_iter)
print next(number_iter)
