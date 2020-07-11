import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()
    if height < 0: # move to write the negative value of data
        t.penup()
        t.left(90)
        t.forward(5)
        t.write(str(height))
        t.backward(5)
        t.right(90)
        t.pendown()
    t.left(90)
    t.forward(height)
    if height >= 0: # move to write the positive value of data
        t.penup()
        t.forward(5)
        t.write(str(height))
        t.backward(5)
        t.pendown()
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


xs = [-48, 117, 200, 240, -160, 260, 220]  # here is the data
maxheight = max(xs)
minheight = min(xs)
numbars = len(xs)
border = 10

if minheight < 0:
    par = minheight - border
else:
    par = 0

wn = turtle.Screen()             # set up the window and its attributes
wn.setworldcoordinates(0-border, par, 40*numbars+border, maxheight+border+5)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.pensize(3)

for a in xs:                  # draw a bar chart
    if a >= 200:
        tess.fillcolor("red")
    elif a >= 100:
        tess.fillcolor("yellow")
    else:
        tess.fillcolor("green")
    drawBar(tess, a)

wn.exitonclick()
