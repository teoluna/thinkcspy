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

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distanceFromPoint(self, otherP):
        dx = (otherP.getX() - self.x)
        dy = (otherP.getY() - self.y)
        return (dy**2 + dx**2) ** 0.5

p = Point(6,7)
q = Point(7,6)

print(p.distanceFromPoint(q))