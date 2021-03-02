import random
import string
WORDLIST_FILENAME = 'words.txt'


def load_words():
    print('Loading word list from file...')
    infile = open(WORDLIST_FILENAME, 'r')
    line = infile.readline()
    wl = line.split()
    print('  ', len(wl), 'words loaded.')
    return wl


wordlist = load_words()


def choose_word(wl):
    return random.choice(wl)


def is_word_guessed(secret_word, letters_guessed):
    judgement = True
    for word in secret_word:
        if word not in letters_guessed:
            judgement = False
    return judgement


def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ''
    for word in secret_word:
        if word in letters_guessed:
            guessed_word += word
        else:
            guessed_word += '_ '
    return guessed_word


def get_available_letters(letter_guessed):
    a = string.ascii_lowercase
    b = ''
    for word in a:
        if word not in letter_guessed:
            b += word
    return b


def hangman(secret_word):
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    letters_guessed = []
    guess_count = 6
    warning_count = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    print('-------------')
    print('You have', warning_count, 'warnings left.')
    while (not is_word_guessed(secret_word, letters_guessed)) and guess_count >= 1:
        print('You have', guess_count, 'guesses left.')
        print('Available letters:', get_available_letters(letters_guessed))
        try_word = input('Please guess a letter:')
        if try_word == '*':
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            print("\n-------------")
        else:
            if str.isalpha(try_word):
                str.lower(try_word)
                if try_word in letters_guessed:
                    if warning_count == 0:
                        guess_count -= 1
                        print("Oops! You've already guessed that letter. You now have no warnings left, "
                              "so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                    else:
                        warning_count -= 1
                        print("Oops! You've already guessed that letter. You now have",
                              warning_count, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
                else:
                    letters_guessed += try_word
                    if try_word in secret_word:
                        print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                    else:
                        print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                        if try_word in vowels:
                            guess_count -= 2
                        else:
                            guess_count -= 1
            else:
                if warning_count == 0:
                    guess_count -= 1
                    print('Oops! That is not a valid letter. You have no warnings left, '
                          'so you lose one guess:', get_guessed_word(secret_word, letters_guessed))
                else:
                    warning_count -= 1
                    print('Oops! That is not a valid letter. You have', warning_count,
                          'warnings left:', get_guessed_word(secret_word, letters_guessed))
            print('-------------')
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        guess_remaining = guess_count
        unique_letters_number = 0
        unique_letters = []
        for word in secret_word:
            if word not in unique_letters:
                unique_letters += word
                unique_letters_number += 1
        the_total_score = unique_letters_number * guess_remaining
        print('Your total score for this game is:', the_total_score)
    else:
        print("Sorry, you ran out of guesses. The word was else.")


def match_with_gaps(my_word, other_word):
    new_word = ''
    for word in my_word:
        if word != ' ':
            new_word += word
    ans = True
    if len(new_word) == len(other_word):
        for i in range(len(new_word)):
            if new_word[i] != other_word[i] and new_word[i] != '_':
                ans = False
    else:
        ans = False
    return ans


def show_possible_matches(my_word):
    k = False
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word, end=' ')
            k = True
    if not k:
        print('No matches found.')




secret_word = choose_word(wordlist)
hangman(secret_word)

