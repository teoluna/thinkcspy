filename = "studentdata.txt"
score = 6

infile = open(filename, 'r')
line = infile.readline()

while line:
    values = line.split()
    if len(values[1:]) > score:
        print(values[0])
    line = infile.readline()

infile.close()