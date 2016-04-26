from collections import deque


def letter_queue(commands):
    q = deque()
    for c in commands:
        if c[0:2] == 'PU':
            q.append(c.split()[-1])
        elif c[0:2] == 'PO':
            if q:
                q.popleft()

    return ''.join(q)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
