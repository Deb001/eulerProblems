def sumSquare(n):
    s = n * (n+1)/2
    return (int) (s * s)

def squareSum(n):
    s= 0
    for i in range(1,n+1):
        s = s + i *i
    return s

print(sumSquare(100) - squareSum(100))
