y=[]
b=[]
n =int(input("Enter count of strings:"))
print("enter the string one by one:") 
for i in range(0, n): 
    a=(input()) 
    y.append(a)
for e in y: 
    if e not in b:
        b.append(e)
print(b)
#method 2
lst=[]
n =int(input("Enter count of strings:"))
print("enter the string one by one:") 
for i in range(0, n): 
    a=(input()) 
    y.append(a)
for i in lst:
    for j in range(i+1,lst):
        if(lst[i]==lst[j]):
            lst.remove(lst[j])
print(lst)
        