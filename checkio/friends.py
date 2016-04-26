from collections import defaultdict

class Friends:
    def __init__(self, connections):
        net = defaultdict(set)
        for c in connections:
            p1, p2 = c
            net[p1].add(p2)
            net[p2].add(p1)
        self.data = net

    def add(self, connection):
        p1, p2 = connection
        if p1 in self.data.keys():
            if p2 in self.data[p1]:
                return False

        self.data[p1].add(p2)
        self.data[p2].add(p1)
        return True

    def remove(self, connection):
        p1, p2 = connection
        if p1 in self.data.keys():
            if p2 in self.data[p1]:
                self.data[p1].remove(p2)
                self.data[p2].remove(p1)
                if not self.data[p1]:
                    del self.data[p1]
                if not self.data[p2]:
                    del self.data[p2]
                return True

        return False

    def names(self):
        return set(self.data.keys())

    def connected(self, name):
        return set(self.data[name])



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])

    assert letter_friends.add({"c", "d"}) is True, "Add"

    assert letter_friends.add({"c", "d"}) is False, "Add again"
    print letter_friends.data

    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
