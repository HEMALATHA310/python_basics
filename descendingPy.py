li=[]
n = int(input("Enter count of numbers:"))
print("enter the number one by one:") 
for i in range(0, n): 
    a=int(input()) 
    li.append(a)
for i in range(0,n):
    for j in range(i+1,n):
        if(li[i]<li[j]):
            sml=li[i]
            li[i]=li[j]
            li[j]=sml
print("ascending order is:",li)
