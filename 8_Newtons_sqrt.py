def newtonSqrt(n):
    approx = 0.5 * n
    for i in range(6):
        betterapprox = 0.5 * (approx + n/approx)
        print(betterapprox)
        approx = betterapprox
    return betterapprox

print(newtonSqrt(25))