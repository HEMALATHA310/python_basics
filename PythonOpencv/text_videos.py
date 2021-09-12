'''
Created on Oct 12, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass
import cv2
capt=cv2.VideoCapture('vv.mp4')#(argument-either filename/device index of cam(0/-1-default))

print(capt.get(cv2.CAP_PROP_FRAME_WIDTH))
print(capt.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(capt.get(cv2.CAP_PROP_FRAME_COUNT))

while(True):
    ret,frame=capt.read()
    #gray=cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2RGB)
    #cv2.imshow('frame',gray)
    
    
    cv2.imshow('frame',frame)
    
    cv2.waitKey(0) & 0xFF 
        



capt.release()
cv2.destroyAllWindows()
