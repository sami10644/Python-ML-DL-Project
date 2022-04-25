import random
words_list = ["Hello","Boy",'book','Loop',"vague"]
def play_game():

    # Pick word randomly from list
    random_num = random.randint(0, (len(words_list) - 1))
    current_word = list(words_list[random_num].upper())
    print(current_word)
    # print('The word has', str(len(current_word)), 'characters')

    picked_letters = []
    correct_ones = []
    for i in range(len(current_word)):
        correct_ones.append('_ ')

    lifes = 5
    while lifes != 0:

        # Check if all characters have been already guessed
        if current_word == correct_ones:
            print('You won!')
            break

        current_letter = input('Pick a letter: ').upper()

        # Check if character has already been chosen
        if current_letter in picked_letters:
            print('You already chose this letter!')
            continue

        # Check if character is in word
        if current_letter in current_word:
            index_list = []
            for i in range(len(current_word)):  # Get indexes of character in word
                if current_word[i] == current_letter:
                    index_list.append(i)

            picked_letters.append(current_letter)  # Append to keep track of chosen characters
            for i in index_list:
                correct_ones[i] = current_letter.upper()  # Append to correct position

            print('Correct!')
            for i in correct_ones:
                print(i + ' ', end='')

        # Incorrect character
        else:
            picked_letters.append(current_letter)
            lifes -= 1
            print('Incorrect')
            print('You have', str(lifes), 'lifes left')
            continue


play_game()
