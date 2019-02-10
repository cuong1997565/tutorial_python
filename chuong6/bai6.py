#cube finder
# def cute_finder(n):
#     cubes = {}
#     for i in range(n+1):
#         cubes[i] = i**3
#     return cubes
# print cute_finder(10)

# word counter
# def word_counter(s):
#     count = {}
#     for char in s:
#         count[char] = s.count(char)
#     return count
# print word_counter('harshit')

user = {}

name = raw_input('What is your name :')
age = input('What is your age :')
fav_movies = raw_input('your fav movies separated by comma').split(',')
fav_songs = raw_input('your fav songs separated by, ').split(',')
user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs
for key, value in user.items():
    print "key :",key , "value :",value 