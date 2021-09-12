'''
Created on Oct 20, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass

import numpy as np
a=np.array([8,7,6,5])
#print("un reversed:",a)
#print(len(a))
l=len(a)
#print(type(l))
for i in range (int(l/2)):
    #print("i",i)
    n=a[i]
    #print('a[i]',a[i])
    a[i]=a[l-i-1]
    #print('a[l-i-1]',a[l-i-1])
    a[l-i-1]=n
    #print('a[l-i-1,1]',a[l-i-1])
print("reversed",a) 



#2D REV ARRAY
li=[]
def rev(a):
#print(len(a))
    l=len(a)
#print(type(l))
    for i in range (int(l/2)):
    #print("i",i)
        n=a[i]
    #print('a[i]',a[i])
        a[i]=a[l-i-1]
    #print('a[l-i-1]',a[l-i-1])
        a[l-i-1]=n
        li.append(a)
    #print('a[l-i-1,1]',a[l-i-1])
    #print("reversed_array:",np.array(li))
    
arr=np.array([[3,2,1],[6,5,4]])
print("un-reversed_array",arr)
rev(arr[0])
rev(arr[1])
print("reversed_array:",np.array(li))
    





        