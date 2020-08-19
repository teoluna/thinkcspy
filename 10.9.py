def sumNegatives(lst):
    negative = []
    for num in lst:
        if num < 0:
            negative.append(num)        
    return sum(negative)