filename = 'alice.words.txt'

maxlength = 0
longest_word = ""

with open(filename, 'r') as infile:
    for line in infile:
        words = line.split()
    
        for w in words:
            if len(w) > maxlength:
                maxlength = len(w)
                longest_word = w
    print(longest_word)

