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
            
    def __str__(self):
        return "h=" + str(self.height) + ", w=" + str(self.width)
        
    def transpose(self):
        # temp = self.height   # третий стакан, переливаем
        # self.height = self.width
        # self.width = temp
        
        self.width, self.height = self.height, self.width # python sugar
        
r = Rectangle(Point(100, 50), 10, 5)
print(r.width)
print(r.height)

r.transpose()
print(r.width)
print(r.height)