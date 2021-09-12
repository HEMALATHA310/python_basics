'''
Created on Oct 27, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass

'''
Created on Oct 27, 2020

@author: aaa
'''

import random as r
import numpy as np
a=np.array([[11,14,31],[7,21,6],[3,8,9]])
np.put(a,np.random.choice(a.size),2)
print("array after replacement:",a)


b=int(input("enter the value to be added"))
row=(r.randrange(len(a)))
col=(r.randrange(len(a)))
a[row][col]=b
print("array after replacement:",a)







