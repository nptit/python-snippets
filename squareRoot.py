class squareRoot():
    def __init__(self, value=0, accuracy=1e-10):
        if value < 0:
            raise ValueError("don't know how to calculate root of a negative number")
        self.value = value
        self.root = 0
        self.accuracy = accuracy

    def binarySearch(self):
        low = 0
        high = self.value + 1

        while True:
            mid = (high - low) / 2.0 + low
            target = mid * mid
            if abs(target - self.value) <= self.accuracy:
                self.root = mid
                return mid
            elif target > self.value:
                high = mid
            elif target < self.value:
                low = mid

    def newtonMethod(self):
        x = self.value + 1
        while True:
            xnew = x - (x**2 - self.value) / (2.0*x)
            if abs(xnew**2 - self.value) <= self.accuracy:
                self.root = xnew
                return xnew
            x = xnew

x = squareRoot(4)
print x.binarySearch()
print x.newtonMethod()

