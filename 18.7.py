class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

class Rectangle:
    """ Rectangle class using Point, width and height. """
    def __init__(self, point_lc, initW, initH):
        self.location = point_lc
        self.width = initW
        self.height = initH

r = Rectangle(Point(4,5), 6, 5)

findxypoint = r.location 
print(findxypoint)