#No 5
# import random
#
# magic_number = random.randrange(1,51)
# counter =0
#
# guess = int(input("Guess the number I'm thinking of: "))
# print(magic_number)
# while counter < 4 :
#
#             if guess < magic_number:
#                 guess = int(input("Too low! Guess again: "))
#             elif guess > magic_number:
#                 guess = int(input("Too high! Guess again: "))
#             else:
#                 print("Winner")
#                 print("You got it in {} guesses! It was {}.".format(counter+1,magic_number))
#                 break
#
#
#             counter += 1
#
#
# if guess != magic_number:
#    print("Loser")

# import random
# number = random.randint(1, 51)
#
#
# number_of_guesses = 0
# print('okay! ',' I am Guessing a number between 1 and 51:')
#
# while number_of_guesses < 5:
#     guess = int(input())
#     number_of_guesses += 1
#     if guess < number:
#         print('Your guess is too low')
#     if guess > number:
#         print('Your guess is too high')
#     if guess == number:
#         break
# if guess == number:
#     print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
# else:
#     print('You did not guess the number, The number was ' + str(number))



#With additional information


# import random
# number = random.randint(1, 51)
#
#
# number_of_guesses = 0
# print('okay! ',' I am Guessing a number between 1 and 51:')
# print(number)
# def c():
#     number_of_guesses = 0
#     while number_of_guesses < 5:
#         guess = int(input())
#         number_of_guesses += 1
#         if guess < number:
#             print('Your guess is too low')
#         if guess > number:
#             print('Your guess is too high')
#         if guess == number:
#             break
#     if guess == number:
#         print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
#     else:
#         print('You did not guess the number, The number was ' + str(number))
#         v = input("do u wnat to play again ?")
#         if v =='y':
#             c()
#         else:
#             pass
# c() #runn
import random


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





#4
# def getNumberList(filename): # Define a function that returns a list of numbers with filename as paramater
#     with open(filename,'r') as f:
#         strList = f.read().split()
#         numberList = [int(num) for num in strList]
#     return numberList
#
# def getAverage(filename, func): # Define a function that returns the average of the numbers from a file, with the filename and the function that returns numbers as parameters
#     numbers = func(filename)
#     return sum(numbers)
#
# def main():
#     filename = input("Input the file name: ")
#     average = getAverage(filename, getNumberList)
#     print(average)


# newFileBytes = [123, 3, 255, 0, 100]
# # make file
# newFile = open("filename.txt", "wb")
# # write to file
# for byte in newFileBytes:
#     newFile.write(byte.to_bytes(1, byteorder='big'))
#
# newFileByteArray = bytearray(newFileBytes)
# newFile.write(newFileByteArray)
#3
# words_list = ["Hello","Boy",'book','Loop',"vague"]
# def play_game():
#
#     # Pick word randomly from list
#     random_num = random.randint(0, (len(words_list) - 1))
#     current_word = list(words_list[random_num].upper())
#     print(current_word)
#     # print('The word has', str(len(current_word)), 'characters')
#
#     picked_letters = []
#     correct_ones = []
#     for i in range(len(current_word)):
#         correct_ones.append('_ ')
#
#     lifes = 5
#     while lifes != 0:
#
#         # Check if all characters have been already guessed
#         if current_word == correct_ones:
#             print('You won!')
#             break
#
#         current_letter = input('Pick a letter: ').upper()
#
#         # Check if character has already been chosen
#         if current_letter in picked_letters:
#             print('You already chose this letter!')
#             continue
#
#         # Check if character is in word
#         if current_letter in current_word:
#             index_list = []
#             for i in range(len(current_word)):  # Get indexes of character in word
#                 if current_word[i] == current_letter:
#                     index_list.append(i)
#
#             picked_letters.append(current_letter)  # Append to keep track of chosen characters
#             for i in index_list:
#                 correct_ones[i] = current_letter.upper()  # Append to correct position
#
#             print('Correct!')
#             for i in correct_ones:
#                 print(i + ' ', end='')
#
#         # Incorrect character
#         else:
#             picked_letters.append(current_letter)
#             lifes -= 1
#             print('Incorrect')
#             print('You have', str(lifes), 'lifes left')
#             continue
#
#
# play_game()

#1
# Create an Menu program that handles two integer variables A & B. them menu will have
# the following options:
# a) Set a new Value for A - will input the user for a new value for A
# b) Set a new Value for B - will input the user for a new value for B
# c) Save to File - will save the values of the variables to a file (data.txt)
# d) Load from File - will load the data of A & B from a text file
# e) Quit - will quit the program

#
# q1=input('question 1:')
# q2=input('question 2:')
# with open('aa.txt','w+') as f:
#     f.writelines(q1+'\n')
#     f.writelines(q2+'\n')
# f = open('aa.txt','r')
# f.close()
#
#
#
# while not os.path.exists(file_path):
#     time.sleep(1)
#
# if os.path.isfile(file_path):
#     # read file
# else:
#     raise ValueError("%s isn't a file!" % file_path)

#2)




# import pickle
# def bin_write():
#     q1=input('question 1:')
#     q2=input('question 2:')
#     with open('result.bin','w+') as w:
#         w.writelines(q1+'\n')
#         w.writelines(q2+'\n')
#
#     # q= open('result.bin','wb')
#     pickle.dump(w)
#     w.close()
#     w = open('result.bin','rb')
#     d1 = pickle.load(w)
#     w.close()
#     for n,y in d1.items():
#         print(n,"-->", y)
# bin_write()

# Change the program in question 2 in the following ways:
# a) make the file binary instead (data.bin)
# b) when the program starts, it load the file if it exists
# c) add exceptions later (after we learn about them in the next lessons)





#

# 6

with open("bb.txt", "r") as text_file:
    data = text_file.readlines()
    a = data[0]
    b = data[1]
a= int(a)
b = int(b)

def play():
    x = random.randint(1, 100)
    guess = 0
    while guess != 5:
        y = int(input("Enter a guess: "))
        if y > x:
            print(" Your guess is too large, guess smaller")
            guess = guess + 1
        if x > y:
            print(" Your guess is too small, guess larger")
            guess = guess + 1
        if x == y:
            print("You guessed correctly, the number was", x)
            break
    #while guess == 5:
    if guess == 5:
        #guess = guess + 1
        v = input("Do you want to play again?")
        if v == "Yes":
            play()
        if v == "No":
            pass


play()
