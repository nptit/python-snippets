def guess_game(lo, hi):
    print "Please think of a number between 0 and 100 [0, 100)!"
    while True:
        guess = new_guess(lo, hi)
        print "Is your secret number {}?".format(guess)
        response = get_user_response()
        if response == 'c':
            print "Game over. Your secret number was: {}".format(guess)
            return guess
        elif response == 'h':
            hi = guess
        elif response == 'l':
            lo = guess

def get_user_response():
    text = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."
    while True:
        response = raw_input(text)
        if response in ['l', 'h', 'c']:
            return response

def new_guess(lo, hi):
    return (lo + hi) / 2


if __name__ == '__main__':
    guess_game(0, 100)
