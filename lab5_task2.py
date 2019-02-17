class Point:
    """This class will have x and y attribute"""
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        print('(%d,%d)' % (self.x, self.y))


class Rectangle:
    """There are width,height and corner attributes"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.corner = Point()
    pass


def find_center(r):
    p = Point()
    p.x = r.corner.x + r.width / 2
    p.y = r.corner.y + r.height / 2
    return p


# s1 = Rectangle(100, 200)
# print(find_center(s1))

def move_rectangle(r, dx, dy):
    p = Point()
    p.x = r.corner.x + dx + r.width / 2
    p.y = r.corner.y + dy + r.height / 2
    return p
