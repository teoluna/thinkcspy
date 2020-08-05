def reverse(astring):
    string = ""
    for char in astring:
        string = char + string
    return string

def is_palindrome(myStr):
    if reverse(myStr) == myStr:
        return True
    else:
        return False