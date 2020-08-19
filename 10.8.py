def sumEven(lst):
    evennums = []
    for num in lst:
        if num % 2 == 0:
            evennums.append(num)        
    return sum(evennums)