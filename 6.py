import random
with open("bb.txt", "r") as text_file:
    data = text_file.readlines()
    a = data[0]
    b = data[1]
a= int(a)
b = int(b)
def play():

    x = random.randint(1,a)
    guess = 0
    while guess != b:
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
