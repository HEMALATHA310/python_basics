li=[]
c=0
n=int(input("enter count of numbers:"))
print("enter number one by one:")
for i in range(0,n):
    a=float(input())
    li.append(a)
print("enter key value:")
key=float(input())
for i in range(0,n):
    if(key==li[i]):
        c=c+1
        print("element found")
        print("element at position:",i+1)
if(c==0):
    print("element not found")