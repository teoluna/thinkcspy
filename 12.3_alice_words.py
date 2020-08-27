filename = "\\Users\\Danylo\\Documents\\github\\alices_adventures_in_wonderland.txt"

wordscount = {}

with open(filename, 'r') as infile:

    for line in infile:
        values = line.split()
        
        for word in values:

            # remove punctuation
            word = word.replace('"', '').replace("'", '').replace('_', '').replace('-', '')
            word = word.replace('.', '').replace(',', '').replace('!', '').replace("?", "")
            word = word.replace('(', '').replace(')', '').replace('[', '').replace(']', '')
            word = word.replace(':', '').replace(';', '').replace('*', '')
            
            # put in lower case
            word = word.lower()

            if word not in wordscount:
                wordscount[word] = 1

            else:
                wordscount[word] += 1
                
    with open('alice.words.txt', 'w') as outfile:

        # alphabetical sorting of all the words
        for i in sorted(wordscount.keys()):
            if i != "":
                #resultword = "i"
                resultcount = wordscount[i]

                # write the results to a text file
                outfile.write("\n" + i + " " + str(resultcount))





