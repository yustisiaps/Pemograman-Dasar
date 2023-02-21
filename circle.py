import math

class Circle:
    # Initial initialization method
    def __init__(sl, x, y, r):
        sl.x = x
        sl.y = y
        sl.r = r

    # Returns the area of a circle
    def Area(sl):
        return math.pi*sl.r*sl.r


