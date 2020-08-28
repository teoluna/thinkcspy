sentence = input("Please enter a sentence")
sentence = sentence.split()

pirate = {"sir":"matey","hotel":"fleabag inn","student":"swabbie",
"boy":"matey","madam":"proud beauty",
"professor":"foul blaggart","restaurant":"galley",
"your":"yer","excuse":"arr","students":"swabbies",
"are":"be","lawyer":"foul blaggart","the":"th’","restroom":"head",
"my":"me","hello":"avast","is":"be","man":"matey"}

translation = []

for word in sentence:
    if word in pirate:
        translation.append(pirate[word])
    else:
        translation.append(word)

print(" ".join(translation))