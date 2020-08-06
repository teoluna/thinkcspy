def remove_all(substr,theStr):
    while theStr.find(substr) != -1:      
        index = theStr.find(substr)
        length = len(substr) + index
        theStr = theStr[:index] + theStr[length:]
    return theStr