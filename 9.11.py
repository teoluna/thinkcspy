def remove(substr,theStr): 
    index = theStr.find(substr)
    if index == -1:
        return theStr
    length = len(substr) + index
    strbegin = theStr[:index]
    strend = theStr[length:]
    newstr = strbegin + strend
    return newstr