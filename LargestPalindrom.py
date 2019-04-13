
import math

def isPalindrom(num):
    rev = 0
    n = num
    while (n != 0):
        rem = n % 10
        rev = rev * 10 + rem
        n = n//10
    if (rev == num):
        return 1
    else:
        return 0


def isPrime(num):
    val = (int) (math.sqrt(num))
    for i in range(2,val +1):
        if num % i == 0:
            return 0
    return 1

def hasDivisor(num,base):
    while (base > 100):
        if (num % base == 0):# check if it is a 2 digit number
            if (num/base < 999):
                return 1
        base = base -1
    return 0


largeNum = 999 * 999
lowNum = 100 * 100
#palindrom = []
while (largeNum > lowNum):
    if (isPalindrom(largeNum)):
        if(isPrime(largeNum) == 0):
#            palindrom.append(largeNum)
            if (hasDivisor(largeNum,999)):
                break
    largeNum -=1
print(largeNum)
#print(palindrom)