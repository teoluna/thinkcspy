import random

def create_list():
    """Creates a list containing 100 random integers between 0 and 1000""""
    alist = []
    for i in range(100):
        i = random.randrange(0, 1000)
        alist.append(i)
    return alist

def average(list):
    """Finds average from a list"""
    for i in list:
        average = sum(list)/len(list)
    return average

list = create_list()
print(list)
print(average(list))