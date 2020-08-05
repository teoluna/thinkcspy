print("x", '\t', "y", '\t', "x*y")  #table column headings
print("---", '\t', "---", '\t', "-----")

for x in range(13):    # generate values for columns
    y = 0
    while y < x:
        y = y + 1
    print(x, '\t', y, '\t', x*y)