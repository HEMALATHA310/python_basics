l=[]
n =int(input("Enter count of string:"))
print("enter the string one by one:") 
for i in range(0, n): 
    a=(input()) 
    l.append(a)
b = []
unique = []
for x in l:
    if x  in b:
        continue
    else:
        b.append(x)

print(l)
#met2
b=[2,3,4,2,5,6,7]
for x in b:
    if x == b[i]:
        continue
    else:
        b.append(x)
print(b)