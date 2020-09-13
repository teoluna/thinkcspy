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
    
    def slope_from_origin(self, point2):
        numerator = (point2.getY() - self.getY())
        denominator = (point2.getX() - self.getX())
        
        if denominator == 0:
            return None

        m = numerator/denominator
        return m
        
p = Point(0,0)
q = Point(0,0)

print(p.slope_from_origin(q))