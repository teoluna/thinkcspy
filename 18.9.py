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
        
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def __str__(self):
        return "h=" + str(self.height) + ", w=" + str(self.width)
    
    def area(self):
        return self.height * self.width

r = Rectangle(Point(0, 0), 10, 5)
print(r.area())