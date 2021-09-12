'''
Created on Oct 13, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass

# Program to multiply two matrices using nested loops 
R1= int(input("Enter the number of rows of  matA:")) 
C1= int(input("Enter the number of columns matA:")) 
R2= int(input("Enter the number of rows of matB:")) 
C2= int(input("Enter the number of columns of matB:")) #p*n/n*q=P*Q
  



#matrix condition=R1*C1 = R2*C2 == R1*C2

if(C1==R2):       
# get input of matrixA 
    matA = []
    print("enter the elements of matA one by one")
    for i in range(R1):#row range
        #print('i',i)           
        c =[] 
        for j in range(C1):#column range
            #print('j',j)
            #c=[]
            c.append(int(input())) 
        matA.append(c)
    print( 'matA:',matA)
           
    matB=[]
    print("enter the elements of matB one by one")
    for i in range(R2):#row range
        #print('i',i)           
        c =[] 
        for j in range(C2):#column range
            #print('j',j)
            #c=[]
            c.append(int(input())) 
        matB.append(c)
    print( 'matB:',matB)
                   
    res =[]
    for i in range(R1):
        c=[]
        for j in range(C2):
            temp=0
            c.append(temp)
        res.append(c)
        print(res)
        
        
    # performing multiplication 
    for i in range(len(matA)):
         
        for j in range(len(matB)):#(column)
            
            for k in range(len(matB)):#(row)
                
                res[i][j] =res[i][j]+ matA[i][k] * matB[k][j] 

    print("the resultant matrix is:")        
    for r in range(R1):
        for s in range(C2):
            print( (res[r][s]), end = " " ) #END PARAMETER-python print() comes with the prameter called 'end' .by default the value of end is'\n'.
        print()
else:
    print("the matrix multiplication is not posible for the above input") 
        
  
      
    
        
         
  
        
        
  
 
  

           

  


     
  

             
  
 
    
    
    
    
    
    
# Program to multiply two matrices (vectorized implementation) 
  
# Program to multiply two matrices (vectorized implementation) 
#import numpy as np 
# take a 3x3 matrix 
#A = [[12, 7, 3], 
    #[4, 5, 6], 
    #[7, 8, 9]] 
  
# take a 3x4 matrix 
#B = [[5, 8, 1, 2], 
    #[6, 7, 3, 0], 
    #[4, 5, 9, 1]] 
  
# result will be 3x4
#result= [[0,0,0,0], 
        #[0,0,0,0], 
       # [0,0,0,0]] 
  
#result = np.dot(A,B) 
  
#for r in result: 
    #print(r)