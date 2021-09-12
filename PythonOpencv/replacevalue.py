'''
Created on Oct 15, 2020

@author: aaa
'''

if __name__ == '__main__':
    pass

li=[]
n=int(input("enter the count:"))
print("enter the numbers:")
for i in range (n):
    a=int(input())
    li.append(a)
print("list:",li)
for i in range(n):
    if(li[i]%2==0):
        li[i]=-2
print("replaced list:",li)
