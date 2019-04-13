import math

'''
When m and n are any two positive integers (m < n):

a = n2 - m2
b = 2nm
c = n2 + m2
Then a, b, and c form a Pythagorean Triple.

a+b+c = 1000
a + b > c as it is a triangle
so c < 500
all the numbers are less than 500
'''
c = 1
m =2
while(c<1000):
    for n in range(1,m+1):
        a=m*m-n*n
        b=2*m*n
        c=m*m+n*n
        if(c>1000):
            break
        if(a==0 or b==0 or c==0):
            break
        if (a + b + c) == 1000:
            print (a*b*c)
    m=m+1


