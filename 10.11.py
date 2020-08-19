def sumUntilEven(lst):
    sumnums = 0
    for num in lst:
        if num % 2 != 0:
            sumnums = sumnums + num      
        if num % 2 == 0:
            break
    return sumnums

print(sumUntilEven([1, 5, 3, 4, 5, 7]))