#28/02
n=int(input("enter the number:"))
s=1
if(n>=0):
    for i in range(n,0,-1):#another method for i in range(1,n+1):
        s=i*s
    print("the factorial of",n,"is:",s)
else:
    print("enter number greater than or equal to 0")
    
    
#INBUILT METHOD
import math
num = input("Enter a number:")
print("The factorial of ",num, " is : ",math.factorial(int(num)))

