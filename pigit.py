__author__ = 'qxu'

import re
def pig_it(text):
    words=text.split()
    for w in words:
        if re.match(r'[\.|!|\?]', w):
            print w
        else:
            print w[1:]+w[0]+'ay'
    pass
    return ' '.join(map(lambda x: x[1:]+x[0]+'ay' if not re.match(r'[\.|!|\?]', x) else x, text.split()))

pig_it('Pig latin is cool')
print pig_it('O tempora o mores !')