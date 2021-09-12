li=[]
n =int(input("Enter count of numbers:"))
print("enter the number one by one:") 
for i in range(0, n): 
    a=float(input()) 
    li.append(a)
min1=li[0]
max1=li[0]
for a in li:
        if(a>max1):
            max1=a
        if(a<min1):
            min1=a
print("minimum:",min1)
print("maximum:",max1)

        
    
    


    

        
    
        