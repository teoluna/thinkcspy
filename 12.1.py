sentence = input("Please enter a sentence")
sentence = sentence.lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
dictsent = {}

for char in sentence:
    if char not in alphabet:
        continue
    if char not in dictsent:
        dictsent[char] = 1
    else:
        dictsent[char] += 1

for i in sorted(dictsent.keys()):  
    print(i, dictsent[i])  