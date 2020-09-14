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
    
    def get_line_to(self, point2):
        m = self.slope_from_origin(point2)
        c = point2.getY() - m * point2.getX()
        return (m, c)
        
p = Point(6,15)
q = Point(4,11)

print(p.get_line_to(q))