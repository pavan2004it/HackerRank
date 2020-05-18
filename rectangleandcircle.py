class Rectangle:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Circle:

    def __init__(self, r: int):
        self.r = r

    def area(self):
        import math
        return math.pi * math.pow(self.r, 2)

