def gcd(a, b):
   if (b == 0):
       return a
   return gcd(b, a%b)

def lcm(a,b):
    return (int) ((a * b) / gcd (a,b))

val = 1
for i in range (2, 20):
    val = lcm(i,val)
print(val)
