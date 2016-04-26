table1 = {0: '', 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
table2 = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 400: 'CD', 20: 'XX', 900: 'CM', 30: 'XXX', 800: 'DCCC', 40: 'XL', 300: 'CCC', 50: 'L', 60: 'LX', 70: 'LXX', 200: 'CC', 80: 'LXXX', 600: 'DC', 90: 'XC', 100: 'C', 700: 'DCC', 500: 'D'}

print set(table1.items()) & set(table2.items())

def toroman(num):
    k = num // 1000
    h = (num - 1000 * k) // 100
    t = (num - 1000 * k - h * 100) / 10
    d = num - 1000 * k - h * 100 - 10 * t
    print k, h, t, d
    print table2[1000*k], table2[100*h], table2[10*t], table2[d]
    pass

print toroman(2999)
