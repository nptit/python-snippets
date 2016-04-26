

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Coordinate({}, {})".format(self.x, self.y)

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'


print Coordinate(1,2) == Coordinate(1,2)
print repr(Coordinate(1,2))


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        inx = intSet()
        for v in self.vals:
            if v in other.vals:
                inx.insert(v)
        return inx

    def __len__(self):
        return len(self.vals)

# x = intSet()
# x.insert(1)
# x.insert(2)

# y = intSet()
# #y.insert(1)

# print x.intersect(y)
# print len(x)


class Queue(object):
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def remove(self):
        try:
            v = self.queue[0]
            del self.queue[0]
            return v
        except:
            raise ValueError("Empty container.")

    def __repr__(self):
        return "Queue({})".format(self.queue)

# q1 = Queue()
# q2 = Queue()
# q1.insert(17)
# q2.insert(20)
# q1.remove()
# q1.insert(100)
# q2.remove()
# q2.remove()
