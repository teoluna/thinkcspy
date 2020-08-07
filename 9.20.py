def remove_dups(astring):
    newstring = ""
    for char in astring:
        if newstring.count(char) == 0:
            newstring += char
    return newstring 

print(remove_dups("mississippi"))   #should print misp
