'''
Created on Oct 16, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass
import numpy as np
a=np.array([3,2,5,9,6,1])
print(a)
#print(type(a))
b=np.array([1,9,6,8,7])
print(b)
#print(type(b))
print("the common element(s):")
#print(np.intersect1d(a,b))#gives the common elements in ascending order
#for i in a:
        #if i in b:
            #print(i)
            
#INTERSECTION
#import numpy as np
#a=np.array([[1,2,3],[4,7,8]])
#print(a[0][1])
#print(type(a))
#b=np.array([[1,2,4],[9,2,5]])
#print(b)
#print(type(b))
#print("the common element(s) through intersection:")
#print(np.intersect1d(a,b))            


#2D ARRAY           
#import numpy as np
a=np.array([[1,2,3],[4,7,8]])
#print(type(a))
b=np.array([[11,66,5],[9,10,5]])
#print(type(b))
print("the common element(s):")
#print(np.intersect1d(a,b))#gives the common elements in ascending order
common_ele=[]
for i in a:
    for j in i:
        for k in b:
            for l in k:
                if(j==l):
                    common_ele.append(l)
print(common_ele)
        
                   
            
    

            
            
