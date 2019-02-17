class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        p = Point()
        if isinstance(other, Point):
            p.x = self.x + other.x
            p.y = self.y + other.y

        elif isinstance(other, tuple):
            p.x = self.x + other[0]
            p.y = self.y + other[1]
        return p

    def __str__(self):
        return 'The sum is (%d,%d)' % (self.x, self.y)


if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(5, 6)
    p3 = p1 + p2
    print(p3)

    p4 = Point(3, 4)
    p5 = (7, 8)
    p6 = p4 + p5
    print(p6)
