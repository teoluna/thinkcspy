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
    
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return (self.x, self.y)
        
p = Point(6,15)
print(p.move(2, 2))