import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square with side sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()       # set up the window and its attributes
wn.bgcolor("lightyellow")

alex = turtle.Turtle()     # create alex
alex.color('darkolivegreen')
alex.pensize(3)

def movingSquare():
    for i in range(20):
        drawSquare(alex, 100)     # call the function to draw the square
        alex.right(18)

movingSquare()
wn.exitonclick()