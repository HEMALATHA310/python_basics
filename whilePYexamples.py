#1.WHILE PRACTISE
#n=int(input("enter limit:"))
x=0
while x<5:
    x+=1
    if x==2:
        pass#when no need o doing nothing
    print(x)
#2.SEARCH USING WHILE
s=[2,3,4,5,6,7]
c=0
key=0
#for i in s:
    #while key==s[i]:
        #c=c+1
    #print("element found")
    #else:
    #print("ele not found")
#3.REPITION STRING
print('*'*3)
print('p'*5)
for i in range(1,10,2):
    print(('*' *i).center(30))#center() holds space from margin may be 10,20...like that
    
