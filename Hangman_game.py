print('H A N G M A N')
user_choice = input('Type "play" to play the game, "exit" to quit: ')

import random

words_list = ['python', 'java', 'kotlin', 'javascript']
guess_word = random.choice(words_list)
guess_word_list = list("-" *(len(guess_word)))

def game():
    lives = 8
    tries_list = []
    while lives > 0:
        print()
        print("".join(guess_word_list))
        user_try = input("Input a letter: ")
        print(lives)
        if "".join(guess_word_list) == guess_word:
            print(f"You guessed the word {guess_word}!")
            print("You survived!")
            break

        if user_try.isascii() and user_try.islower():
            if len(user_try) > 1 or len(user_try) == 0:
                print("You should input a single letter")
            elif user_try in tries_list:
                print("You already typed this letter")
            else:
                if user_try not in set(guess_word):
                    lives -= 1
                    print("No such letter in the word")
                    tries_list.append(user_try)
                else:
                    indices = [index for index, letter in enumerate(guess_word) if letter == user_try]
                    for d in indices:
                        guess_word_list[d] = user_try
                    tries_list.append(user_try)
        else:
            print("You should input a single letter" if len(user_try) > 1 else "It is not an ASCII lowercase letter")
    else:
        print('You are hanged!')


if user_choice == 'play':
    game()
else:
    exit()