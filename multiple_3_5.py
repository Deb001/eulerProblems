
def multipleCount(num, cap):
    retVal = 0
    nextNum = 0

    if (num == 0 or cap == 0):
        print("either num or cap is 0")
        return retVal
    while (cap > nextNum):
        retVal = retVal + nextNum
        nextNum = nextNum + num
    return retVal

def multCount(cap):
    sum = 0
    for i in range(1,cap):
        if (i%3 == 0 or i%5 == 0):
            sum = sum + i
    return sum

s1 = multipleCount(3,1000) + multipleCount(5,1000) - multipleCount(15,1000)

print("***** Ans *****")
print( s1)
print(multCount(1000))
