# example = [[1,2,3],[1,2,3],[1,2,3]]
# nested_comp = [[i for i in range(1,4)] for j in range(3)]
# print nested_comp

# new_list = []
# for j in range(3):
#     new_list.append([1,2,3])
# print new_list

# square = {num : num**2 for num in range(1,11)}
# for v,k in square.items():
#     print "Square of "+str(v)+" is: "+ str(k)

# string = "Harshit"
# word_count = {char:string.count(char) for char in string}
# print word_count

# odd_even =  {i:('even' if i%2==0 else 'odd') for i in range(1,11)}
# print odd_even

#sets comprehension ---> only one video
s = { k**2 for k in range(1,11)}
print s

names = ['harshit','mohit','rohit']
first = {name[0] for name in names}
print first