def reverse(astring):
    string = ""
    for char in astring:
        string = char + string
    return string

string = "apple"
reverse(string)