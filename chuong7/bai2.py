# even_nums = [i for i in numbers if i%2 == 0]
# even_num2 = [i for i in range(1,11) if i%2 == 0]
# odd_num   = [i for i in range(1,11) if i%2 != 0]
# print even_num2
# print odd_num


###########
# def num_to_string(l):
#     return [str(i) for i in l if (type(i) == int or type(i) == float)]
# print num_to_string([True,False,[1,2,3],1,1.0,3])

#############
# nums = [1,2,3,4,5,6,7,8,9,10]
# new_list = []
# for i in nums:
#     if i%2 == 0:
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print new_list

# new_list2 = [i*2 if (i%2 == 0) else -i for i in nums]
# print new_list2

#list comprehension in nested list 
# example = [[1,2,3],[1,2,3],[1,2,3]]
# nested_comp = [[i for i in range(1,4)] for j in range(3)]
# print nested_comp

#list comprehension summary
# square = []
# for i in range(1,11):
#     square.append(i**2)
# print square

square = [i ** 2 for i in range(1,11)]
print square