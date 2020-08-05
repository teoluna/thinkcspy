def remove_letter(theLetter, theString):
    string = ""
    for achar in theString:   
        if achar != theLetter:
            string = string + achar
    return string
