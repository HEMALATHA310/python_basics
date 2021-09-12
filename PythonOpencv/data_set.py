'''
Created on Oct 27, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass

               
import numpy as np
from numpy import genfromtxt
data = genfromtxt('submission.csv',dtype=None,encoding=None, delimiter=',')#delimiter keyword to define splitting
print("data:",data)

#textfile

data1 = genfromtxt('data.txt',dtype=None,encoding=None,delimiter=',')#by default gentxt uses dtype=float
print("txt data:",data1)                                   #.that is why string columns are converted to 'nan'.



#exl file
data2 =np. genfromtxt('dataset.xlsx',dtype=None,encoding=None, delimiter=',')
print("xlsx data:",data2)


#import csv
#with open('submission.csv', 'r') as f:
    #w = list(csv.reader(f, delimiter=';'))
    #print(w[:7])


