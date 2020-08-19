def countWords(lst, wordlen=5):
    counter = 0
    for word in lst:
        if len(word) == wordlen:
            counter = counter + 1        
    return counter

print(countWords(["How", "many", "words", "with", "length", "5", "are", "there"]))