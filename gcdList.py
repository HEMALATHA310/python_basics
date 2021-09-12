li=[]
n = int(input("Enter count of numbers:"))
print("enter the number one by one:") 
for i in range(0, n): 
    a=int(input()) 
    li.append(a)
x=li[0]
y=li[1] 
for a in li:
    if(x>y):
        s=y
    else:
        s=x
for z in range(1,s+1):
    if(x%z==0):
        if(y%z==0):
            gcd=z
print("gcd is:",gcd)
    

    