import turtle

def drawPoly(turtle, sides, size):
    """Make turtle someturtle draw a square with somesides somesize."""
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)

wn = turtle.Screen()       # set up the window and its attributes
wn.bgcolor("lightyellow")

alex = turtle.Turtle()     # create alex
alex.color('darkolivegreen')
alex.pensize(3)

drawPoly(alex, 8, 50)