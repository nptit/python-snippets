def convert(numerator, denominator):
    p, r = divmod(numerator, denominator)
    main = str(p) + '.'

    if r == 0:
        return main

    # fraction part
    remainder, digits = [r], []
    while r:
        p, r = divmod(r*10, denominator)
        digits.append(str(p))

        if r in remainder:
            idx = remainder.index(r) # index for the repeating remainder
            strx = ''.join(digits[:idx]) + '(' + ''.join(digits[idx:]) + ')'
            return main + strx

        remainder.append(r)

    return main + ''.join(digits)




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
