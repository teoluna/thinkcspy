import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()       # set up the window and its attributes
wn.bgcolor("lightyellow")

alex = turtle.Turtle()     # create alex
alex.color('darkolivegreen')
alex.pensize(3)

def growingSquare(x):
    size = 10
    for counter in range(x):
        size = size + 20
        drawSquare(alex, size)    # call the function to draw the square
        alex.penup()
        alex.right(90)            # move alex to the starting position for the next square
        alex.forward(10)
        alex.left(90)
        alex.forward(-10)
        alex.pendown()

growingSquare(5)
wn.exitonclick()
