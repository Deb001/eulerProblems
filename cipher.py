'''
Given a ciphertext encrypted with Caesar cipher, find the corresponding plaintext.
Encryption in Caesar cipher is done by replacing each letter with a letter 3 positions to the left,
e.g. 'a' is replaced with 'x', 'b' with 'y', ..., 'd' with 'a' and so on.
You need to fill in a function that takes as input a string,
the cipher text and sets the output variable to the corresponding plaintext. The ciphertext contains only lowercase alphabets.
Input: nrfzh
Output: quick
'''

import math
def isPrime(num):
    val = (int) (math.sqrt(num))
    for i in range(2,val +1):
        if num % i == 0:
            return 0
    return 1

def nthPrime(range, n):
    if n == 0 or n > range:
        return -1
    num = 2
    count = 1
    while (count < n and num < range):
        if (isPrime(num)):
            count = count + 1
        num = num + 1
    return num -1
# print(nthPrime(1000,50))


ip = "nrfzh"

op = []
str = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l = len(ip)
j = 0
for i in range (0,l):
    j = str.index(ip[i]) + 3
    if (j >= 25):
        j = j - 26
    op.append(str[j])
print (op)

