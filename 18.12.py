class Point:
    """ Point class for x, y coordinates """
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
        
class Rectangle:
    """ Rectangle class of width, heigth using Point class """
    def __init__(self, initP, initW, initH):
        self.loc = initP
        self.width = initW
        self.height = initH
        
    def contains(self, point):
        """ Checks if a Point is in open upper bounds of Rectangle """
        if point.x < 0 or point.y < 0:
            return False
        
        if point.x < self.width and point.y < self.height:
            return True
        else:
            return False
        
r = Rectangle(Point(0, 0), 10, 5)

#tests
print(r.contains(Point(0, 0)))
print(r.contains(Point(3, 3)))
print(r.contains(Point(3, 7)))
print(r.contains(Point(3, 5)))
print(r.contains(Point(3, 4.99999)))
print(r.contains(Point(-3, -3)))