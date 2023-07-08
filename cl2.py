class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __floordiv__(self, other):
        return Point(self.x // other.x, self.y // other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)


p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = p1 + p2
p4 = p2 - p1
p5 = p2 // p1
p6 = p2 * p1
print(p3.x, p3.y)
print(p4.x, p4.y)
print(p5.x, p5.y)
print(p6.x, p6.y)

