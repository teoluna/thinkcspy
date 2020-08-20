filename = "studentdata.txt"

infile = open(filename, 'r')
line = infile.readline()

while line:
    values = line.split()
    sumscore = 0
    for i in values[1:]:
        sumscore += int(i)
    average = sumscore/len(values[1:])
    print("Student's name: " + str(values[0]) + ", Average grade: " + str(average))
    line = infile.readline()

infile.close()