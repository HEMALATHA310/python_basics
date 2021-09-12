li=[]  
odd=[]
even=[]
n =int(input("Enter count of number: "))
print("the numbers are:") 
for i in range(0, n): 
    a=float(input()) 
    li.append(a) 
for a in li:
    if(a%2==0):
        even.append(a)
    else:
        odd.append(a)
print("even number:",even)
print("odd number:",odd)
    