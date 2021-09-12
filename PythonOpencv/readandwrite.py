'''
Created on Oct 11, 2020

@author: aaa
'''


if __name__ == '__main__':
    pass

import cv2
img=cv2.imread('APJ.jpg',1)#(1st ARGUMENT-filename 2nd argument-flag(0,1,-1))

#img=cv2.imread('APJwer.jpg',1) WRONG FILENAME/WRONG PATH GIVES 'NONE' ON PRINT STATEMENT
print(img)#WILL GIVE THE MATRIX OF IMAGE AS OUTPUT
cv2.imshow('image',img)#(1st ARGUMENT-image name 2nd argument-img variable)
                        #DISPLAY THE IMAGE
w=cv2.waitKey(0) & 0xFF#COUNTS IN ms THE ACTUAL TIME THE IMAGE TO BE DISPLAYED
cv2.destroyAllWindows()

#if w == ord('s'):
cv2.imwrite('apj_copy.png',img)#(1st ARGUMENT-imgname 2nd argument-img to be saved i.e(img variable))
# cv2.destroyAllWindows()
