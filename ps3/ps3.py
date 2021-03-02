import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    s = word
    s.lower()
    first_component = 0
    for i in s:
        first_component += SCRABBLE_LETTER_VALUES[i]
    word_length = len(s)
    a = 7 * word_length - 3 * (n - word_length)
    second_component = max([a, 1])
    return first_component * second_component
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')  # print all on the same line
    print()  # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels + 1, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    hand["*"] = hand.get("*", 0) + 1
    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    hand2 = hand.copy()
    for i in word:
        if i in hand:
            if hand2[i] > 1:
                hand2['i'] -= 1
            else:
                del hand2[i]
    return hand2


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    k = True
    m = []
    for i in word:
        if i not in hand:
            k = False
            break
        m.append(i)
    if '*' in m:
        x = m.index('*')
        ma = m[::]
        me = m[::]
        mi = m[::]
        mo = m[::]
        mu = m[::]
        ma[x] = 'a'
        me[x] = 'e'
        mi[x] = 'i'
        mi[x] = 'o'
        mo[x] = 'u'
        a = ''
        e = ''
        i = ''
        o = ''
        u = ''
        for n in range(len(m)):
            a += ma[n]
            e += me[n]
            i += mi[n]
            o += mo[n]
            u += mu[n]
        if a in word_list or e in word_list or i in word_list or o in word_list or u in word_list:
            pass
        else:
            k = False
    else:
        if word not in word_list:
            k = False
    return k


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    count = 0
    for item in hand:
        count += hand[item]
    return count


def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """
    n = calculate_handlen(hand)
    total_score = 0
    while True:
        print("Current hand:", end=' ')
        display_hand(hand)
        word = input('Enter word, or "!!" to indicate that you are finished: ')
        if word == '!!':
            print('Total score for this hand:', total_score)
            print("----------")
            break
        else:
            if is_valid_word(word, hand, word_list):
                score = get_word_score(word, n)
                total_score += score
                print('"' + word + '"', 'earned', score, 'points.', 'Total:', total_score, 'points')
                print("\n")
                hand = update_hand(hand, word)
            else:
                print("That is not a valid word. Please choose another word.")
                hand = update_hand(hand, word)
                print("\n")
            if calculate_handlen(hand) == 0:
                print('Run out of letters. Total score for this hand:', total_score)
                print("----------")
                break
    return total_score


#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    if letter not in hand:
        return hand
    else:
        if letter in VOWELS:
            v = list(VOWELS)
            v.remove(letter)
            x = random.choice(v)
            hand[x] = hand.get(x, 0) + hand[letter]
        if letter in CONSONANTS:
            c = list(CONSONANTS)
            c.remove(letter)
            x = random.choice(c)
            hand[x] = hand.get(x, 0) + hand[letter]
        del hand[letter]
        return hand


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    total_number = int(input('Enter total number of hands: '))
    hand_size = 7
    all_hands_score = 0
    for i in range(total_number):
        hand = deal_hand(hand_size)
        print('Current hand:', end=' ')
        display_hand(hand)
        ans = input('Would you like to substitute a letter? ')
        if ans == 'yes':
            letter = input('Which letter would you like to replace: ')
            hand = substitute_hand(hand, letter)
            print("\n")
        if ans == 'no':
            print('\n')
        sc = play_hand(hand, word_list)
        all_hands_score += sc
        ans2 = input("Would you like to replay the hand? ")
        if ans2 == 'yes':
            all_hands_score -= sc
            ab = play_hand(hand, word_list)
            all_hands_score += ab
    print("Total score over all hands: ", all_hands_score)


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
