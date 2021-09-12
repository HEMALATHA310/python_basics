#wrong program
g=[]
c=0
n =int(input("Enter count of numbers:"))
print("enter the number one by one:") 
for i in range(0, n): 
    a=int(input()) 
    g.append(a)
print("enter key value:")
key=(input())#should not have key without data type if it is will be assigned to string and will not consider it
for i in range(0,n):
    if (g[i]==key):
        c=c+1
        print("element found at position:",i)
if(c==0):
    print("element not found")



    