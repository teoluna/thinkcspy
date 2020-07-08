import turtle

def drawPoly(someturtle, somesides, somesize):
    """Make turtle someturtle draw a square with somesides somesize."""
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360/somesides)

wn = turtle.Screen()       # set up the window and its attributes
wn.bgcolor("lightyellow")

alex = turtle.Turtle()     # create alex
alex.color('darkolivegreen')
alex.pensize(3)

drawPoly(alex, 8, 50)