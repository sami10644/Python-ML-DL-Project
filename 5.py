# import random
#
#
# def play():
#     x = random.randint(1, 100)
#     guess = 0
#     while guess != 5:
#         y = int(input("Enter a guess: "))
#         if y > x:
#             print(" Your guess is too large, guess smaller")
#             guess = guess + 1
#         if x > y:
#             print(" Your guess is too small, guess larger")
#             guess = guess + 1
#         if x == y:
#             print("You guessed correctly, the number was", x)
#             break
#     #while guess == 5:
#     if guess == 5:
#         #guess = guess + 1
#         v = input("Do you want to play again?")
#         if v == "Yes":
#             play()
#         if v == "No":
#             pass
#
#
# play()


import random
number = random.randint(1, 51)


number_of_guesses = 0
print('okay! ',' I am Guessing a number between 1 and 51:')

def c():
    number_of_guesses = 0
    while number_of_guesses < 5:
        guess = int(input())
        number_of_guesses += 1
        if guess < number:
            print('Your guess is too low')
        if guess > number:
            print('Your guess is too high')
        if guess == number:
            break
    if guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        print('You did not guess the number, The number was ' + str(number))
        v = input("do u wnat to play again ?")
        if v =='y' or v =='yes':
            c()
        else:
            pass
c()
# import random
# answer = random.randint(1, 100)
# guess = int(input())
# if guess != answer
#       if guess < answer:
#         print("too low")
#         print("Please! Try again")
#
# else:
#    print("you win")
#

