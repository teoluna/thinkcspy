import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.end_fill()
    t.penup()          # move to write the value of the data
    t.backward(height)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(5)
    t.write(str(height))
    t.forward(-5)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.pendown()


xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()             # set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border+5)
wn.bgcolor("mistyrose")

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("maroon")
tess.fillcolor("rosybrown")
tess.pensize(3)


for a in xs:                  # draw a bar chart
    drawBar(tess, a)

wn.exitonclick()
