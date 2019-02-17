class Point:
    """This class will have x and y attribute"""
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)
    pass


"""This is a function called distance_between_points"""


def distance_between_points(t1,t2):
    a = abs(t2.x - t1.x)  # (x2-x1)
    b = abs(t2.y - t1.y)  # (y2-y1)
    import math
    distance = math.sqrt((a**2 + b**2))
    return distance


if __name__ == "__main__":

    s1 = Point(1, 2)
    s2 = Point(4, 6)
    print(distance_between_points(s1, s2))

