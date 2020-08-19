def countOdd(lst):
    oddnums = []
    for num in lst:
        if num % 2 != 0:
            oddnums.append(num)        
    return len(oddnums)