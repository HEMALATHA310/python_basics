#sum of series
n=int(input("enter the number of terms:"))
#a=int(input("enter the value of x:"))
s=1
for i in range(2,n+1):
    if(i%4==0):
        s=s-i
        print(i)
    else:
        s=s+i
    i=i+2
print("the sum of series is:",s)
#next series
a=int(input("enter no:"))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
print(round(sum1,2))