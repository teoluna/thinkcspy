#implement function that works like .count() method

def count(lst, value):
    counter = 0
    for i in lst:
        if i == value:
            counter = counter + 1
    return counter

list = ['apple', 'banana', 'grape', 'apple']
print(count(list, 'apple'))

#implement function that works like .reverse() method

def reverse(lst):
    newlist = []
    index = 0
    for i in lst:
        index = index + 1
        value = lst[-index]
        newlist.append(value)   
    return newlist

lst = [1, 2, 3, 4, 1, 2, 6]
print(reverse(lst))
      
#implement function that works like .insert() method

def insert(lst, pos, elem):
    start = lst[:pos]
    middle = [elem]
    end = lst[pos:]
    newlist = start + middle + end
    return newlist

vowel = ['a', 'e', 'i', 'u']
print(insert(vowel, 3, 'o'))

#implement function that works like .index() method

def index(lst, element):
    result = None
    for i in range(len(lst)):
        if lst[i] == element:
            result = i
            break
    if result == None:
        raise ValueError ("'" + element + "' is not in list")
    return result
    
vowels = ['a', 'e', 'o', 'i', 'u', 'i']        
print(index(vowels, 'ii'))

#implement function that works like in keyword

def is_in(lst, element):
    for i in lst:
        if i == element:
            return True
    return False




