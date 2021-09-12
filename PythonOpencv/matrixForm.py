'''
Created on Oct 13, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass

a = int(input("Enter the number of rows:")) 
b = int(input("Enter the number of columns:")) 
  
matli = [] #list to hold elements
print("Enter the elements one by one:") 
  
# using for to append elements in list
#c=[] 
for i in range(a):#row range
    #print('i',i)           
    c =[] 
    for j in range(b):#column range
        #print('j',j)
        #c=[]
        c.append(int(input())) 
    matli.append(c)#ele added to list
    print('c',c)
    print('matli',matli)

  
#to print the elements list in form of matrix 
for i in range(a):
    #print('i',i) 
    for j in range(b):
        #print('j',j)     
        print( (matli[i][j]), end = " " ) #END PARAMETER-python print() comes with the prameter called 'end' .by default the value of end is'\n'.
    print() 
    

    
    
    #END PARAMETER EXAMPLE
#print("welcome to",end='')
#print("ball",end='')
