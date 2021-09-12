'''
Created on Nov 5, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass

#height and width of coloured img including channels
import cv2
import numpy as np
img=cv2.imread('APJ.jpg',1)#(1st ARGUMENT-filename 2nd argument-flag(0,1,-1))
d=img.shape#gives the dimension in tuple(height,width,channels) 
h=img.shape[0]#height
w=img.shape[1]#width
print(img)
print("dimensions:",d)
print("height:",h)
print("width:",w)

#NOTE:for gray image their no channel displayed

#for i in range(h):
    #for j in range(w):
        #print('img',img[i,j],end='\t')
    #print('\t')