y=[]
ol=[]
n =int(input("Enter count of strings:"))
print("enter the string one by one:") 
for i in range(0, n): 
    a=(input()) 
    y.append(a)
for e in y:
    if e in ol:
        continue
    ol.append(e)
print(ol)