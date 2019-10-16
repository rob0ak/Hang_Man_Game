import random


def set_up_game(word, list_of_letters, blank_list):
    for letter in word:
        list_of_letters += letter
        blank_list += "-"


def find_letters(word_list, blank_list, guess, list_of_guesses):
    count = 0
    # Checks the users guess to see if its within the word_list
    for letter in word_list:
        if letter == guess:
            print("correct")
            blank_list[count] = guess
        count += 1
        if guess not in list_of_guesses:
            list_of_guesses += guess
    # Compares list_of_guesses and blank_list to remove letters that don't belong in the list_of_guesses
    for letter in list_of_guesses:
        if letter in blank_list:
            list_of_guesses.remove(user_guess)


def check_for_win(word_list, blank_list):
    if word_list == blank_list:
        return True
    else:
        return False


def get_char():
    user_input = input("Guess a letter from A-Z: ").upper()
    allowed_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while len(user_input) != 1 or user_input not in allowed_chars:
        user_input = input("Guess a letter from A-Z: ").upper()
    return user_input

def text_animation(wrong_count):
    animation = (
    """
    |-----
    |     |
    |
    |
    |
    |------------
    """,
    """
    |-----
    |     |
    |     O
    |
    |
    |------------
    """,
    """
    |-----
    |     |
    |     O
    |     |
    |
    |------------
    """,
    """
    |-----
    |     |
    |     O
    |     |\ 
    |
    |------------
    """,
    """
    |-----
    |     |
    |     O
    |    /|\ 
    |
    |------------
    """,
    """
    |-----
    |     |
    |     O
    |    /|\ 
    |    /
    |------------
    """,
    """
    |-----
    |     |
    |     O
    |    /|\ 
    |    / \ 
    |------------
       """
    )
    return animation[wrong_count]


list_of_words = ["strengthen","Hello","therapeutic","vegetable","chemical"]
word_choice = random.choice(list_of_words).upper()
letters_in_word = []
blank_word_list = []
wrong_guesses = []
set_up_game(word_choice, letters_in_word, blank_word_list)
hang_man = True

while hang_man:
    print(text_animation(len(wrong_guesses)))
    print(blank_word_list)
    print(f'Guesses: {wrong_guesses}')
    user_guess = get_char()
    find_letters(letters_in_word, blank_word_list, user_guess, wrong_guesses)
    if check_for_win(letters_in_word, blank_word_list):
        print("Congratulations you won!!! :)")
        break
    if len(wrong_guesses) > 5:
        print('Sorry you lose! :(')
        print(text_animation(len(wrong_guesses)))
        break
