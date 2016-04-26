
class myList(object):
    def __init__(self, values = None):
        self.data = [None]
        if values:
            self.data.extend(values)

    def __empty__(self):
        return True if not self.data[0] and len(self.data) == 1 else False

    def __getitem__(self, i):
        if i == 0:
            raise IndexError("1 based list index, 0 not allowed")
        else:
            if self.__empty__():
                raise LookupError("Empty list")
            elif i > len(self.data) - 1:
                raise IndexError("Out of bound error")
            else:
                return self.data[i]

    def __len__(self):
        return len(self.data) - 1

    def __str__(self):
        return str(self.data)


ml = myList([1,2,3])

print ml[4]
