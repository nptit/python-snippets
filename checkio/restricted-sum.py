def checkio(data):
    if len(data) == 1:
        return data[0]
    elif len(data) == 0:
        return 0

    return data[0] + checkio(data[1:])

if __name__ == '__main__':
    print checkio([1,2, 3])
