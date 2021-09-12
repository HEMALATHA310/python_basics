l=[]
n=int(input("enter count:"))
print("enter values:")
for i in range(0,n):
    a=float(input())
    l.append(a)
print("enter key:")
key=(input())
for i in range(0,n):
    if(l[i]==key):
        print("found")
print("element at position:",i)