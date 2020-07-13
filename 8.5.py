import random
import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()

t1.shape('turtle')
t2.shape('circle')

def move_randomly(w, t):
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(150)
    
def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX >= rightBound or turtleX <= leftBound:
        stillIn = False
    if turtleY >= topBound or turtleY <= bottomBound:
        stillIn = False

    return stillIn

def areColliding(t1, t2):
    if t1.distance(t2) < 2:
        return True
    else:
        return False

t1.forward(150)
t2.backward(150)

while (isInScreen(wn, t1) or isInScreen(wn, t2)) and not areColliding(t1, t2):
    if not isInScreen(wn, t1):
        t1.backward(150)
    else:
        move_randomly(wn, t1)
    if not isInScreen(wn, t2):
        t2.backward(150)
    else:
        move_randomly(wn, t2)

wn.exit()