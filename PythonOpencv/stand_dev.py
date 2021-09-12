'''
Created on Oct 27, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass
import numpy as np
a=np.array([1,2,3,4,5,6])
n=len(a)
mean=(sum(a))/n
#print("mean",mean)
c=[]
for i in  a:
    #print(i)
    
    b=i-mean
    #print(b)
    c.append(b)
    
#print("sum of data-mean",sum(c))
#sqrt
s=[]
for i in c:
    d=i**2
    #print('d',d)
    s.append(d)
sqroot_mean=sum(s)
#print("sum of sqrt of mean",sqroot_mean)
variance=(sqroot_mean/(n-1))
s_d=(variance**2)
print("standard deviation of a is",s_d)

#2D ARRAY
li=[]
def std_dev(arr):
    n=len(a)
    mean=(sum(a))/n
#print("mean",mean)
    c=[]
    for i in  arr:
    #print(i)
    
        b=i-mean
    #print(b)
        c.append(b)
    
#print("sum of data-mean",sum(c))
#sqrt
    s=[]
    for i in c:
        d=i**2
    #print('d',d)
        s.append(d)
    sqroot_mean=sum(s)
#print("sum of sqrt of mean",sqroot_mean)
    variance=(sqroot_mean/(n-1))
    s_d=(variance**2)
    li.append(s_d)
    #print("standard deviation of a is",s_d)
    
arr1=np.array([[3,2,1],[6,5,4]])
std_dev(arr1[0])
std_dev(arr1[1])
print("standard deviation of a is",np.array(li))


        



    
    