'''
Created on Nov 5, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass
import cv2

img=cv2.imread('APJ.jpg',1)
p=img[100,100]#pixel can be accessed by it rows and columns,but for BGR it returnd blue,green,red values
print('bgr',p)
#print(p[1])
#acsessing blue pixel
b=img[100,100,0]
print('blue',b)



#modifying values of pixel
img[100,100]=[0,103,121]
print(img[100,100])
#print(p)
#cv2.imshow('image',img)#(1st ARGUMENT-image name 2nd argument-img variable)
                        #DISPLAY THE IMAGE
#w=cv2.waitKey(0) & 0xFF#COUNTS IN ms THE ACTUAL TIME THE IMAGE TO BE DISPLAYED
#cv2.destroyAllWindows