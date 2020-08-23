import turtle

file = 'labdata.txt'
t = turtle.Turtle(shape = 'circle')    # create turtle t 

def transform_data(file):
    """Function that reads the data from file and 
    creates a tuple of (x, y) coordinates"""
    infile = open(file, 'r')
    line = infile.readline()
    
    result = []
    while line:
        values = line.split()
        coord = (int(values[0]), int(values[1]))
        result = result + [coord]
        line = infile.readline()
 
    infile.close()
    return result

def findRegression():
    """Calculates y-points according to formulas"""
    data = transform_data(file)
    #print(data)
    
    n = len(data)                      # number of points 
    
    x_sum = 0
    for tup in data:
        x_sum += tup[0]                # count sum of all x (1082)
    
    x_mean = x_sum/n                   # count mean x (54.1)
    
    y_sum = 0
    for tup in data:
        y_sum += tup[1]
        
    y_mean = y_sum/n                   # count mean y
    
    # find m
    # step 1: numerator
    numerator = 0
    for tup in data:
        numerator_temp = (tup[0]*tup[1]) - (n*x_mean*y_mean)
        numerator += numerator_temp
        
    # step 2: denominator
    denominator = 0
    for tup in data:
        denominator_temp = (tup[0] ** 2) - (n*(x_mean ** 2))
        denominator += denominator_temp
        
    # step 3: calculate m
    m = numerator/denominator
    
    # calculate y according to the formula
    y_best = []
    for tup in data:
        y = y_mean + m*(tup[0] - x_mean)
        y_best += [y]
    
    return y_best

def plotRegression():
    """Uses a turtle t to draw a best fit line through the points with color"""
    data = transform_data(file)
    
    x_list = [int(i[0]) for i in data]
    y_list = findRegression()
    
    maxheight = max(y_list)
    minheight = min(y_list)
    numbars = len(y_list)
    border = 10

    if minheight < 0:
        par = minheight - border
    else:
        par = 0

    wn = turtle.Screen()             # set up the window and its attributes
    wn.setworldcoordinates(0-border, par, 40*numbars+border, maxheight+border+5)
    wn.bgcolor("lightgreen")
    
    # plot points
    for i in range(len(x_list)):
        turtle.penup()
        turtle.setposition(x_list[i], y_list[i])
        turtle.stamp()

    # plot best y
    turtle.penup()
    turtle.setposition(0, 0)
    turtle.color('blue')
    
    y_best = findRegression()
    
    for i in range(len(x_list)):
        turtle.setposition(x_list[i], y_best[i])
        turtle.pendown()

    return (min(x_list), min(y_list), max(x_list), max(y_list))
    
    wn.exitonclick()

plotRegression()