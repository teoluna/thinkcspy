import turtle

def drawSpiral(t, sz):
    """Make turtle t draw a spiral with line length sz."""
    t.forward(-sz)
    t.left(90)
    t.forward(sz)
    t.left(90)
        
def growingSpiral(x):
    size = 3
    for counter in range(x):
        size = size + 5
        drawSpiral(alex, size)    # call the function to draw the square        
        
wn = turtle.Screen()              # set up the window and its attributes
wn.bgcolor("lightyellow")

alex = turtle.Turtle()            # create alex
alex.color('darkolivegreen')

growingSpiral(50)
wn.exitonclick()
