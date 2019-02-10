# def reverse_list(l):
#     l.reverse()
#     return l
# numbers = [1,2,3,4]
# print reverse_list(numbers)

# [4,3,2,1]
# def reverse_list(l):
#     r_list = []
#     for i in range(1, len(l)+1):
#         poped_item = l.pop()
#         r_list.append(poped_item)
#     return r_list
# numbers = [1,2,3,4]
# print reverse_list(numbers)

# def reverse_elements(l):
#     elements = []
#     for i in l:
#         elements.append(i[::-1])
#     return elements
# words = ['abc','tuv','xyz']
# print reverse_elements(words)


#[[2, 4, 6], [1, 3, 5, 7]]
# def filter_old_even(l):
#     odd_nums = []
#     even_nums = []
#     for i in l:
#         if i % 2 == 0:
#             odd_nums.append(i)
#         else:
#             even_nums.append(i)
#     output = [odd_nums,even_nums]
#     return output
# numbers = [1,2,3,4,5,6,7]
# print filter_old_even(numbers)

#[1, 2]
# def common_folder(l1, l2):
#     output = []
#     for i in l1:
#         if i in l2:
#             output.append(i)
#     return output
# print common_folder([1,2,4,5],[1,2,7,8])

#0
def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
        return count
mixed = [1,2,3,[1,3],[1,4]]
print sublist_counter(mixed)