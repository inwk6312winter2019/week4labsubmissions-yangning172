class Point:
    def __init__(self,x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return 'The poin is (%d,%d)' % (self.x, self.y)

    def __add__(self, other):
        p = Point()
        p.x = self.x + other.x
        p.y = self.y + other.y
        return p


if __name__ == '__main__':
    p = Point(3, 4)
    p1 = Point(5, 6)
    p2 = p + p1
    print(p2)

