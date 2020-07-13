def print_triangular_numbers(n):
    i = 1
    while i < n + 1:
        t = int((i*(i+1))/2)
        print(i, "\t", t)
        i = i + 1

print_triangular_numbers(5)