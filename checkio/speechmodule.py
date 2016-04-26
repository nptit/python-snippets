FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
FIRST19 = FIRST_TEN + SECOND_TEN

def checkio(number):
    'converting a number to english word, 0<=number<999'
    if number == 0:
      return FIRST19[number]

    words = []
    h, n = divmod(number, 100)
    if h > 0:
      words.append(FIRST19[h])
      words.append(HUNDRED)

    if 0 < n < 20:
      words.append(FIRST19[n])
    elif n >= 20:
      t, d = divmod(n, 10)
      words.append(OTHER_TENS[t - 2])
      if d:
        words.append(FIRST19[d])

    return ' '.join(words)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print checkio(100)
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
