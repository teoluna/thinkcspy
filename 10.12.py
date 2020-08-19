def count(lst):
    occurence = 0
    index = 0
    while index < len(lst) and lst[index] != "sam":
        occurence = occurence + 1
        index = index + 1
    return occurence + 1

print(count(["mat", "ken", "alex", "sam", "fred"]))