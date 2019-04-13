import math
import time

def isPrime(num):
    if(num == 2):
        return 1
    if (num % 2 == 0):
        return 0
    val = (int) (math.sqrt(num))
    for i in range(2,val +1):
        if num % i == 0:
            return 0
    return 1


def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes


'''

maxNum = 10000 #
n = 1
prime = [2]

start = time.time()
while ( n < maxNum -1):
    n = n+2
    if isPrime(n):
        prime.append(n)


s = 0
max_sum = 0
max_index = 1
l = len(prime)
i = 0
j = 0

while (i < l):
    s = prime[i]
    j = i + 1
    index = 1
    while (j < l):
        s = s + prime[j]
        index = index + 1
        if isPrime(s):
            if ((index > max_index) and (s < maxNum) and (max_sum < s)):
                max_sum = s
                max_index = index
#                print("loop: ", i, "values: ", prime[j], "sum: ", s, "max_sum: ", max_sum, "index: ", index)
        j = j + 1
    i = i + 1


print(max_sum)
print(max_index)
'''
start = time.time()
print(get_primes(1000000))
print(time.time() - start)

