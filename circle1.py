import math

class Circle:
    def __init__(sl, x, y, r):
        sl.x = x
        sl.y = y
        sl.r = r

    def Area(sl):
        return math.pi*sl.r*sl.r