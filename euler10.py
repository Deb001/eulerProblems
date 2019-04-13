import math
def isPrime(num):
    val = (int) (math.sqrt(num))
    for i in range(2,val +1):
        if num % i == 0:
            return 0
    return 1

maxNum = 2000000 # First 3 primes are 2, 3 and 5
sum = 2 + 3 + 5
n = 5
while (n < maxNum):
    n = n + 2
    if isPrime(n):
        sum += n
print(sum)