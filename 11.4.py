import turtle

file = 'labdata.txt'

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

def plotRegression(t):
    """Uses a turtle t to plot the points 
    and draw a best fit line through the points"""
    
    x_list = [int(i[0]) for i in transform_data(file)]
    y_list = findRegression()
    
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    
    # plot points
    for i in range(len(x_list)):
        t.color('blue')
        t.penup()
        t.setposition(x_list[i], y_list[i])
        t.stamp()
        print(x_list[i], y_list[i])
        
    # plot best y
    t.penup()
    t.setposition(0, 0)
    t.color('red')
    for i in range(len(x_list)):
        t.setposition(x_list[i], y_list[i])
        t.pendown()
        
    wn.exitonclick()

tess = turtle.Turtle(shape = 'classic')    # create turtle tess
plotRegression(tess)