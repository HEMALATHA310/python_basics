#2D ARRAY
import numpy as np
li=[]
def M1(a):
    n=len(a)
    mean=(sum(a))/n
    #print(mean)
    li.append(mean)
    
def ascending(a):
    n=len(a)
#for arranging in ascending order
    for i in range(0,n):
        for j in range(i+1,n):
            if(a[i]>a[j]):
                lar=a[i]
                a[i]=a[j]
                a[j]=lar
    #print("ascending order is:",a)
li1=[]
def M2(a):
    ascending(a)
    n=len(a)    
    if(n%2==0):
        x=int(n/2)
        #print("x",x)
        y=int(((n/2)+1))
        #print("y",y)
        median=((a[x-1]+a[y-1])/2)
        li1.append(median)
        print("median ",li1)
        #j=int(median)
        
    else:
        median=((n/2)+1)
        #print("m",median)
        j=int(median)
        k=a[j-1]
        li1.append(k)
        #print("median",k)
        #print("the position where median is found is:",int(median))
arr=np.array([[1,2,3,4],[4,5,6]])
M1(arr[0])
M1(arr[1]) 
M2(arr[0]) 
M2(arr[1])  
print("mean",(li))
print("median",(li1))