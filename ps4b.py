from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord_v2(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    ## bad algorithn when n is bigger
    if n > 7:
        return None

    from itertools import permutations

    letters = [k for k, v in hand.items() for _ in range(v)]
    possible_words= set([''.join(w) for i in range(1, len(letters)+1) for w in permutations(letters, i)])
    valid_words = [w for w in possible_words if w in wordList]

    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    # Create a new variable to store the best word seen so far (initially None)
    best_word = None
    # For each word in the wordList
    for word in valid_words:
        # Find out how much making that word is worth
        score = getWordScore(word, n)
        # If the score for that word is higher than your best score
        if score > max_score:
            # Update your best score, and best word accordingly
            max_score = score
            best_word = word

    # return the best word you found.
    return best_word

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    # Create a new variable to store the best word seen so far (initially None)
    best_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word

    # return the best word you found.
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    # Keep track of the total score
    total_score = 0

    # As long as there are still letters left in the hand:
    while True:
        # Display the hand
        print "Current Hand: ",
        displayHand(hand)
        # Ask user for input
        import time

        t0 = time.clock()
        word = compChooseWord(hand, wordList, n)
        t1 = time.clock()
        word2= compChooseWord_v2(hand, wordList, n)
        t2 = time.clock()
        print "Computer chosen method 1: {}, method 2: {}, t1={}, t2={}".format(word, word2, t1-t0, t2-t1)
        # If the input is a single period:
        if not word:
            # End the game (break out of the loop)
            break
        else:
            word_score = getWordScore(word, n)
            total_score += word_score
            print '\"{}\" earned {} points. Total: {} points\n'.format(word, word_score, total_score)
            # Update the hand
            hand = updateHand(hand, word)
            if sum(hand.values()) == 0:
                print "Total score: {} points.".format(total_score)
                return

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print "Total score: {} points.".format(total_score)


def getUserInput(prompt, valid_commands):
    while True:
        userinput = raw_input(prompt)
        if userinput not in valid_commands:
            print "Invalid command."
        else:
            return userinput
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    hand = {}
    while True:
        userinput = getUserInput("Enter n to deal a new hand, r to replay the last hand, or e to end game:", ['n', 'e', 'r'])
        if userinput == 'n':
            hand = dealHand(HAND_SIZE)
        elif userinput == 'r' and not hand:
            print "You have not played a hand yet. Please play a new hand first!"
            continue
            '''
            try:
                hand
            except:
                print "You have not played a hand yet. Please play a new hand first!"
                continue
            '''
        elif userinput == 'e':
            return

        mode = getUserInput("Enter u to have yourself play, c to have the computer play:", ['u', 'c'])
        if mode == 'u':
            playHand(hand, wordList, HAND_SIZE)
        else:
            compPlayHand(hand, wordList, HAND_SIZE)



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    #compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
    #compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
    playGame(wordList)


