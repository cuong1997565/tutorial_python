user_info = {
    'name' : 'harshit',
    'age'  : 24,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale']
}
#check if key exits in dictionary
# if 'name' in user_info:
#     print 'present'
# else:
#     print 'not present'

#check if value exits in dictionary
# if '24' in user_info.values():
#     print 'present'
# else:
#     print 'not present'

# loops in dictionary
# for i in user_info.values():
#     print i

#value method 
# user_info_value = user_info.values()
# print user_info_value
# print type(user_info_value)

# user_info_key = user_info.keys()
# print user_info_key
# print type(user_info_key)

# loops in dictionary
# for i in user_info:
#     print user_info[i]

#items methods
# user_items = user_info.items()
# print user_info
# print type(user_items)

for key, value in user_info.items():
   print "key :",key + " value : ", value