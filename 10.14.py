def replace(s, old, new):
    newstring = ''
    for i in range(len(s)):
        if s[i] == old:
            newstring = newstring + new
        else:
            newstring = newstring + s[i]
    return newstring

s = 'I love spom! Spom is my favorite food. Spom, spom, spom, yum!'
print(replace(s, 'om', 'am'))