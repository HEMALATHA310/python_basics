li=[]  
leap=[]
notleap=[]
n = int(input("Enter count of years:"))
print("the years are:") 
for i in range(0, n): 
    a=int(input()) 
    li.append(a) 
for a in li:
    if(a%4==0):
        leap.append(a)
    elif(a%400==0):
        leap.append(a)
    elif(a%100==0):
        notleap.append(a)
    else:
        notleap.append(a)
print("leap year:",leap)
print("not a leap year:",notleap)
    

