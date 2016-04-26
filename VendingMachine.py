class Product(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VendingMachine(object):
    def__init__(self):
        self.products = {}

    def addProduct(self, Product, n):
        if Product in self.products:
            self.products[Product] += n
        else:
            self.products[Product] = n

    def checkStock(self, Product):
        try:
            return self.products[Product]
        except:
            return 0

    def order
