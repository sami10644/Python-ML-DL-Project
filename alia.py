# #random numbers:
# #1
# import random
# random.randint(0,18)
#
# #2
# choices_list = [rock, paper, scissors]
#
# print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
# # make sure the input is valid
# options_list = ["0", "1", "2"]
# while True:
#     player_choice_str = input("> ")
#     if player_choice_str not in options_list:
#         print("Invalid choice. Type 0 for Rock, 1 for Paper or 2 for Scissors.")
#     else:
#         break
#
# # change the data type now, should be safe now since we are sure it's one of the valid options
# player_choice = int(player_choice_str)
# print(choices_list[player_choice])
#
# # computer's choice
# cpu_choice = random.randint(0, 2)
# print("Computer chose:")
# print(choices_list[cpu_choice])
#
# # evaluate the result
# # if the same, it's a tie
# if player_choice == cpu_choice:
#     print("It's a tie.")
# # cases when the player wins: (rock and scissors) or (paper and rock) or (scissors and paper)
# elif (player_choice == 0 and cpu_choice == 2) or\
#         (player_choice == 1 and cpu_choice == 0) or\
#         (player_choice == 2 and cpu_choice == 1):
#     print("You win.")
# # anything else means the cpu wins
# else:
#     print("You lose.")

#3
#when guess = magic
#with if

#modified code
# import random
#
# magic_number = random.randrange(1,51)
# counter =0
#
# guess = int(input("Guess the number I'm thinking of: "))
#
# while counter < 4 :
#
#             if guess < magic_number:
#                 guess = int(input("Too low! Guess again: "))
#             if guess ==magic_number:
#                 print("Winner")
#                 print("You got it in {} guesses! It was {}.".format(counter+1,magic_number))
#                 break
#             elif guess > magic_number:
#                 guess = int(input("Too high! Guess again: "))
#
#
#             counter += 1
#
#
# if guess != magic_number:
#    print("Loser")
#fsdhjkgfdsjkjhdfd    ddddd jkhdfjkhlikjdxcfhjkdfjkdffddfdffdkjhjkhkjdfjkdf

#A fraction is represented in the form of 'x/y', where 'x' is the numerator and 'y' is the denominator. The numerator represents the total number of parts taken into account. Whereas, the denominator represents the total number of equal parts in a fraction. The top number in a fraction is always considered a numerator.

x1 = float(input())
y1= float(input())
x2 = float(input())
y2 = float(input())
if y1 == y2:
    print(f'{x1+x2} --- {y1}')
else:
    v = y1 *y2
    X1 = v/y1

    X2 = v/y2
    if x2 ==1:
        pass
    else:
        X2 = x2*X2
    print(f'{X1+X2} ---- {v}')


