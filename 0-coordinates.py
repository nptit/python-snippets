
class coordinates(object):
    npoints = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        coordinates.npoints = coordinates.npoints + 1

    def __repr__(self):
        return "coordinates({},{})".format(self.x, self.y)

    def __str__(self):
        return "<{},{}>".format(self.x, self.y)

# c = coordinates(1, 2)
# print c
# c.z = 10
# print c
# print c.z

# print c.npoints

# c2 = coordinates(3,4)
# print c.npoints
# print c2.npoints
# print coordinates.npoints


class MyClass(object):
    limit = 1

    def __init__(self):
        self.data = []

    def item(self, i):
        return self.data[i]

    def add(self, e):
        if len(self.data) >= self.limit:
            raise Exception("Too many elements")
        self.data.append(e)


# c = MyClass()
# c.add(1)
# MyClass.limit = 2
# c.add(1)


