def countWords(lst):
    counter = 0
    for word in lst:
        if len(word) == 5:
            counter = counter + 1        
    return counter

print(countWords(["How", "many", "words", "with", "length", "5", "are", "there"]))