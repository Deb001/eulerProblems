import math
def isPrime(num):
    val = (int) (math.sqrt(num))
    for i in range(2,val +1):
        if num % i == 0:
            return 0
    return 1

index = 4 # First 3 primes are 2, 3 and 5
n = 5
while (index <= 10001):
    n = n + 2
    if isPrime(n):
        index += 1
print(n)


