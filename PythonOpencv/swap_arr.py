'''
Created on Oct 20, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass
#for i in range(0,10):
    #print(i)
#SWAP FOR !D ARRAY
import numpy as np
a=np.array([1,2,3,4])
print("before swap A:",a)
#print(type(a))
b=np.array([5,6,8,7])
print("before swap B:",b)
temp=a
a=b
b=temp
print("After swap A:",a)
print("After swap B:",b)

# SWAP FOR 2D ARRAY
import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print("before swap A:",a)
#print(type(a))
b=np.array([[5,6,8,7],[4,3,2,1]])
print("before swap B:",b)
temp=a
a=b
b=temp
print("After swap A:",a)
print("After swap B:",b)

