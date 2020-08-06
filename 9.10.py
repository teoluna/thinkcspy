def count(substr,theStr):
    num = 0  
    while theStr.find(substr) != -1:      
        index = theStr.find(substr)
        num = num + 1
        length = len(substr) + index
        theStr = theStr[length:]
    return num