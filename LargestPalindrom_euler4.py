
# Euler 4: Find the largest palindrome made from the product of two 3-digit numbers
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

largeNum = 999 * 999
lowNum = 100 * 100
while (largeNum > lowNum):
    if (isPalindrom(largeNum)):
        break
    largeNum -=1
print(largeNum)
