import turtle

def drawSpiral(t, angle):
    """Make turtle t draw a spiral with angle."""
    line_length = 3
    t.forward(line_length)
    t.left(angle)
    line_length = line_length + 5
           
wn = turtle.Screen()              # set up the window and its attributes
wn.bgcolor("lightyellow")

alex = turtle.Turtle()            # create alex
alex.color('darkolivegreen')

drawSpiral(alex, 90)        
wn.exitonclick()
