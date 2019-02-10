# #zip function 
# user_id = ['user1','user2','user3']
# name    = ['harshit','mohit','rohit']
# last_names = ['vashistha','vashistha','sharma']

# # ('user','harshit'), ('user2','mohit')
# print list(zip(user_id,name,last_names))

# example = [('a',1),('b',2)]
# print dict(example)

l1 = [1,3,5,7]
l2 = [2,4,6,8]
# l = [(1,2),(3,4),(5,6),(7,8)]
#* operator with zip
# l1, l2 = zip(*l)
# print list(l1)
# print list(l2)
new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))
print new_list