class Kls(object):
    def __init__(self, data):
        self.data = data

    def printd(self):
        print(self.data)

    @staticmethod
    def smethod(*arg):
        print('Static:', arg)

    @classmethod
    def cmethod(*arg):
        print('Class:', arg)

c = Kls(1)

c.printd()
c.smethod(2)
c.cmethod(2)

Kls.cmethod(2)
Kls.smethod(2)

Kls.printd()
