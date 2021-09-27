"""
VERSION 1.0
All work and code is the creation of P.Lowther
"""

import random
import string


def return_random_word(word_list):
    # Takes a list and returns the value at a randomised position in the list
    return word_list[random.randint(0, len(word_list))]


def convert_list_to_string(list_to_convert):
    return ''.join(list_to_convert)


def check_if_guess_in_word(guess_one):
    # Returns True if the guess_one appears in the random word variable
    return guess_one in random_word


def replace_stars_with_characters(list_to_check, player_guesses_to_check):
    # check's the player's guesses against the random_word string.
    # If the random word contains any of the player's guesses then the output list is amended with the letter
    # This removes the * at the same position as the random_word and replaces with the correct character
    for value, letter in enumerate(list_to_check):
        if letter in player_guesses_to_check:
            out_list[value] = letter


def check_if_player_won(word_after_guess):
    # Return true if there are no *'s in the string which means the player has guessed all characters correctly
    return '*' not in word_after_guess


def remove_and_update_potential_guesses(remaining_alphabet, players_guess):
    # remove the letter and return back as a string
    lst1 = list(remaining_alphabet)
    for letter in lst1:
        if players_guess == letter:
            lst1.remove(letter)
            # added a break here as it will just continue to iterate over the list even if found
            break
    return lst1


def update_console_to_show_stick_figure(player_lives_left):
    if player_lives_left == 7:
        return
    elif player_lives_left == 6:
        print('_______')
    elif player_lives_left == 5:
        print('_______')
        print('|')
        print('|')
        print('|')
        print('|')
        print('_______')
    elif player_lives_left == 4:
        print('_______')
        print('|	  |')
        print('|     O')
        print('|')
        print('|')
        print('_______')
    elif player_lives_left == 3:
        print('_______')
        print('|	  |')
        print('|     O')
        print('|    /|')
        print('|')
        print('_______')
    elif player_lives_left == 2:
        print('_______')
        print('|	  |')
        print('|     O')
        print('|    /|\\')
        print('|')
        print('_______')
    elif player_lives_left == 1:
        print('_______')
        print('|	  |')
        print('|     O')
        print('|    /|\\')
        print('|    /')
        print('_______')
    elif player_lives_left == 0:
        print('_______')
        print('|	  |')
        print('|     O')
        print('|    /|\\')
        print('|    / \\')
        print('_______')


list_of_words = []
player_lives = 7
player_guesses = []
out_list = []
game_on = True
# create a string of all of the alphabet representing the letters not guessed.
potential_guesses = string.ascii_lowercase

with open('word_list.txt') as my_new_file:
    contents = my_new_file.read()
    # read the words from the text file and return as a list with white space removed
    for word in contents.split('\n'):
        list_of_words.append(word.strip())

# Pick random word
random_word = return_random_word(list_of_words)

# Create a list of *'s to be shown to the player
for item in random_word:
    out_list.append('*')

# Welcome message
print('Welcome to Hangman!')
print('You have seven attempts to guess the word!')
print('Your potential guesses are: ', ''.join(potential_guesses))

while game_on:

    print(f'You have {player_lives} guesses remaining!')
    print(convert_list_to_string(out_list))
    # validate user input
    while True:
        try:
            player_guess = input('Please enter your next guess: ')
            # Make player's guess all lower case
            player_guess = player_guess.lower()
            if player_guess == '':
                raise SyntaxError
            # check if player_input is in the remaining alphabet. 'in' can be slow but it's okay for this list's size
            if player_guess not in potential_guesses or len(player_guess) > 1:
                raise ValueError
        except ValueError:
            print('Please enter a valid remaining letter!')
        except SyntaxError:
            print('Please enter something!')
        else:
            break
    player_guesses.append(player_guess)
    potential_guesses = remove_and_update_potential_guesses(potential_guesses, player_guess)
    print('Your remaining potential guesses are: ', ''.join(potential_guesses))
    if check_if_guess_in_word(player_guess):
        replace_stars_with_characters(random_word, player_guesses)
    else:
        player_lives -= 1
        print('WRONG!')

    update_console_to_show_stick_figure(player_lives)
    if player_lives <= 0:
        print('you lose'.upper())
        print(f'Correct word was: {random_word}')
        game_on = False
        break
    if check_if_player_won(out_list):
        print(random_word)
        print('congratulations you win'.upper())
        game_on = False
        break