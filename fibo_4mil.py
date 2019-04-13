maxNum=4000000
def nextFibo(fibo1, fibo2):
    return fibo1+ fibo2


fib1 = 1
fib2 = 2
evenFiboSum = 2
loop = 1
fibN = nextFibo (fib1, fib2)
while (fibN < maxNum):
    if (fibN % 2 == 0 ):
        evenFiboSum = evenFiboSum + fibN
    temp = fib1 + fib2
    fib1 = fib2
    fib2 = temp
    fibN = nextFibo(fib1, fib2)
print (evenFiboSum)

