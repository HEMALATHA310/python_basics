'''
Created on Oct 12, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass
import cv2

img=cv2.imread('APJ.jpg',1)
import numpy as np
#img=np.zeros([512,512,3],np.uint8)

img=cv2.line(img,(0,0),(67,90),(0,0,255),4)#arguments like srt co-ord,ending co-ord,color,thickness
img=cv2.arrowedLine(img,(0,255),(78,85),(0,255,0),7)
img=cv2.rectangle(img,(384,0),(78,98),(255,0,0),-1)
img=cv2.circle(img,(67,98),6,(255,0,255),10)

font=cv2.FONT_HERSHEY_DUPLEX
img=cv2.putText(img,'text',(30,50),font,2,(255,255,0),3,cv2.LINE_4)
#img=cv2.imwrite('APJ_copy.jpg',1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()