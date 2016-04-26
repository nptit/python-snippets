class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.x = west
        self.y = south
        self.wx = width_WE
        self.wy = width_NS
        self.height = height

    def corners(self):
        x = self.x
        y = self.y
        wx = self.wx
        wy = self.wy
        return {"north-west": [y+wy, x], "north-east": [y+wy, x+wx],\
                "south-west": [y, x], "south-east": [y, x+wx]}

    def area(self):
        return self.wx * self.wy

    def volume(self):
        return self.wx * self.wy * self.height

    def __repr__(self):
        return "%s(%r, %r, %r, %r, %r)" \
            % (self.__class__.__name__, self.y, self.x, self.wx, self.wy, self.height)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
