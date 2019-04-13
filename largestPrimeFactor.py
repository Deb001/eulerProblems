def maxPrimeFact(n):
    factors = []
    f = 2
    while (n>1):
        if (n % f == 0): #f is a factor
            factors.append(f)
            n = n/f
        else:
            f = f + 1
    return max(factors)

max = maxPrimeFact(600851475143)
print(max)