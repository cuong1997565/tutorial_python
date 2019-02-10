# # function returning two values
# def func(int1, int2):
#     add = int1 + int2
#     multiple = int1 * int2 
#     return add, multiple
# print func(5,6)

# something more about tuples, list, str
# nums = tuple(range(1,11))
# print nums

########
user_info = {
    'name' : 'harshit',
    'age'  : 24,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale']
}
print user_info['age']
print type(user_info)


#how to add to empty dictionary
user_info2 = {}
user_info2['name'] = 'mohit'
print user_info2