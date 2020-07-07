import turtle

num_of_sides = int(input("Enter the number of sides of a regular polygon:"))
length_of_side = int(input("Enter the length of the side:"))
color = input("Enter the color name or hex value of color (# RRGGBB): ")

# create turtle pen
wn = turtle.Screen()
anna = turtle.Turtle()

anna.fillcolor(color)
anna.begin_fill()

# draw the polygon
for i in range(num_of_sides):
    anna.forward(length_of_side)
    anna.left(360/num_of_sides)

anna.end_fill()
wn.exitonclick()
