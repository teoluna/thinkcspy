import random

def create_list():
    alist = []
    for i in range(100):
        alist.append(random.randrange(0, 1000))
        alist.sort()
    return alist

def max_value(alist):
    return alist[0]

alist = create_list()
print(alist)
print(max_value(alist))