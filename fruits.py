

def nfruits(d_fruits, s_eat):
    for fruit in s_eat[:-1]:
        for k in d_fruits:
            d_fruits[k] += 1
        d_fruits[fruit] -= 2

    d_fruits[s_eat[-1]] -= 1

    return max(d_fruits.values())



print nfruits({'A': 1, 'B': 2, 'C': 3}, 'AC')
print nfruits({'I': 7, 'E': 9, 'D': 6, 'T': 10}, 'EE')
print nfruits({'P': 9, 'T': 7, 'O': 6}, 'O')
print nfruits({'U': 5, 'Z': 7, 'E': 6, 'T': 6, 'P': 10}, 'UUU')
print nfruits({'A': 10, 'B': 10, 'K': 7, 'R': 9, 'U': 6, 'Y': 8, 'Z': 10}, 'ZZRY')
