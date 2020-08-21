filename = 'studentdata.txt'

infile = open(filename, 'r')
line = infile.readline()

while line:
    values = line.split()
    intvalues = [int(x) for x in values[1:]]
    minscore = min(intvalues)
    maxscore = max(intvalues)
    print(values[0], minscore, maxscore)
    line = infile.readline()

infile.close()