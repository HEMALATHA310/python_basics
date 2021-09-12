g=[]
n =int(input("Enter count of string:"))
print("enter the string one by one:") 
for i in range(0, n): 
    a=(input()) 
    g.append(a)
print(g)
print("enter the pos of strings which are to be swapped:")
x=int(input())
y=int(input())
temp=g[x]
g[x]=g[y]
g[y]=temp
print("the swapped list is:",g)
    







