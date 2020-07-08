import turtle

def drawPoly(turtle, n, size):
    """Make turtle draw a polygon with n-sides of size."""
    for i in range(n):
        turtle.forward(size)
        turtle.left(360/n)

wn = turtle.Screen()       # set up the window and its attributes
wn.bgcolor("lightyellow")

alex = turtle.Turtle()     # create alex
alex.color('darkolivegreen')
alex.pensize(3)

drawPoly(alex, 8, 50)