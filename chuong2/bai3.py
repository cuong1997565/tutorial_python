# winning_number = 43
# guess = 1
# number = int(input("guess a number between 1 and 100 :"))
# game_over = False 

# while not game_over:
#     if number == winning_number:
#         print "you win, and you guessed this number in ", guess , " times "
#         game_over = True
#     else:
#         if number < winning_number:
#             print "too low"
#         else:
#             print "too high"
#         guess += 1
#         continue


num = input("enter a number :")
for num in range(1,num):
    if num % 2 == 0 :
       print "so chia he cho 2 :",num
    else:
       print "so khong chia het cho 2 :",num 
