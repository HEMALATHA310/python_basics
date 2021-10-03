'''
Created on Oct 3, 2021

@author: aaa
'''

if __name__ == '__main__':
    pass
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
#print("removed_even numbers are:",even)
print("List after removing even no.s:",odd)
    