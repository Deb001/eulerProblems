import math
import time

def isPrime(num):
    if(num == 2):
        return 1
    if (num %2 == 0):
        return 0
    val = (int) (math.sqrt(num))
    for i in range(2,val +1):
        if num % i == 0:
            return 0
    return 1

def rotations(num):
    str_num = (str) (num)
    str_len = len(str_num)
    n = str_len
    ret_val = []
    while (n > 0):
        str_num = str_num[1:] + str_num[0]
        n = n-1
        ret_val.append((int)(str_num))
    return ret_val

def isAllPrime(arr):
    status = 1
    for i in arr:
        status = status * isPrime(i)
        if status == 0:
            break
    return status


maxNum = 1000000 # First 3 primes are 2, 3 and 5
sum = 3
n = 5
rot_list = []
start = time.time()
while (n < maxNum):
    n = n + 2
    if isPrime(n):
        rot_list = rot_list + rotations(n)
        if isAllPrime(rot_list):
            sum += 1
        rot_list = []
print(time.time() - start)
print(sum)