def mySqrt(n):
    oldguess = n/2
    for i in range(1, int(n+1)):
        oldguess = (1/2) * (oldguess + (n/oldguess))
    return int(oldguess)