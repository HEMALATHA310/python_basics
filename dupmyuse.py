y=[]
n =int(input("Enter count of strings:"))
print("enter the string one by one:") 
for i in range(0, n): 
    a=(input()) 
    y.append(a)
for i in range(0,n):
   # print("y[i]",y[i])
    for j in range(i+1,n):
        #print("y[j]",y[j])
        if y[i]==y[j]:
            y.remove(j)#y.remove(j)
#ValueError: list.remove(x): x not in list
#will not work with

print(y)
