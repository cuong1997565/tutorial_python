# add and delete data 
user_info = {
    'name' : 'harshit',
    'age'  : 24,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale']
}

# how to add data
# user_info['fav_songs'] = ['song1', 'song2']
# print user_info

# how to remove data 
# poped_item = user_info.pop('fav_tunes')
# print "popped item is :", poped_item
# print user_info

#popitem method 
# popped_item = user_info.popitem()
# print user_info
# print popped_item

######## update json 
more_info = { 'name' : 'harshit vashish', 'state' : 'Haryana'}
user_info.update(more_info)
print user_info