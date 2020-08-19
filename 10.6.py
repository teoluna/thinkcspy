def sum_of_squares(xs):
    result = []
    for i in xs:
        result.append(i ** 2)
    return sum(result)

print(sum_of_squares([2, 3, 4]))
print(sum_of_squares([0, 1, -1]))
print(sum_of_squares([5, 12, 14]))