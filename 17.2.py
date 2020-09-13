class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    
    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def __str__(self):
        return f"x={self.x}, y={self.y}"

    def reflect_x(self):
        return Point(self.x, (self.y * (-1)))
        
p = Point(3,7)
print(p.reflect_x())