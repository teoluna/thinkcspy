def print_triangular_numbers(n):
    for i in range(1, n+1):  # generate values for columns
        t = int((i*(i+1))/2)
        print(i, "\t", t)

print_triangular_numbers(5)