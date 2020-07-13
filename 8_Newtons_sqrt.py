def newtonSqrt(n):
    approx = 0.5 * n
    betterapprox = 0.5 * (approx + n/approx)
    while betterapprox != approx:
        approx = betterapprox
        betterapprox = 0.5 * (approx + n/approx)
        print("Approximate result:", betterapprox)
    return betterapprox

print("Final result:", newtonSqrt(25))