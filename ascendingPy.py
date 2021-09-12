li=[6,5,4,3,2,1]
n = len(li)#int(input("Enter count of numbers:"))
#print("enter the number one by one:") 
#for i in range(0, n): 
    #a=int(input()) 
    #li.append(a)
for i in range(0,n):
    for j in range(i+1,n):
        if(li[i]>li[j]):
            lar=li[i]
            li[i]=li[j]
            li[j]=lar
print("ascending order is:",li)
