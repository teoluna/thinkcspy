import math

def is_rightangled(a, b, c):
    a_count = round((math.sqrt(b ** 2 + c ** 2)), 4)
    b_count = round((math.sqrt(a ** 2 + c ** 2)), 4)
    c_count = round((math.sqrt(a ** 2 + b ** 2)), 4)
    if a_count == round(a, 4):
        return True
    elif b_count == round(b, 4):
        return True
    elif c_count == round(c, 4):
        return True
    else:
        return False