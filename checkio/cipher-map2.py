def getmaskpos(cipher_grille):
    'given cipher, return tuples of positions in mask'
    return [(i,j) for i,row in enumerate(cipher_grille) for j, x in enumerate(row) if x == 'X']

# def rotate_ccw90(data):
#     'roatate a matrix 90 degree counterclockwise'
#     return zip(*[row[::-1] for row in data])

def rotate_cw90(data):
    'roatate a matrix 90 degree clockwise'
    return zip(*data[::-1])

def recall_password(cipher_grille, ciphered_password):
    mask = cipher_grille
    data = ciphered_password

    password = []
    for i in range(4):
        pos = getmaskpos(mask)
        password.extend([data[i][j] for i,j in pos])
        mask = rotate_cw90(mask)

    return ''.join(password)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
