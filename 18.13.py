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
                
    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
        
r = Rectangle(Point(0, 0), 10, 5)
print(r.diagonal())