'''
Created on Oct 12, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass
import cv2
capt=cv2.VideoCapture('vv.mp4')#(argument-either filename/device index of cam(0/-1-default))
while(True):
    ret,frame=capt.read()
    cv2.imshow('frame',frame)
    
    cv2.waitKey(0) & 0xFF 
        



capt.release()
cv2.destroyAllWindows()
