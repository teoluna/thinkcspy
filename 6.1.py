import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("palegreen")

alex = turtle.Turtle()
alex.color("darkgreen")
alex.pensize(3)

def move(t,s):
    """Move turtle t away for distance s and draw a square."""
    
    for i in range(5):
        drawSquare(alex,20) # call the function to draw the square
        t.penup()
        t.forward(s)
        t.pendown()
        
move(alex,40)
wn.exitonclick()
