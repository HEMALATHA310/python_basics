#method1
import math
a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
print("gcd of a and b is",math.gcd(a,b))
#method2
x=int(input("Enter the number x:"))
y=int(input("Enter the number y:"))
if(x>y):
    s=y
else:
    s=x
for z in range(1,s+1):
    if(x%z==0):
        if(y%z==0):
            gcd=z
print("gcd of x and y is:",gcd)
    
