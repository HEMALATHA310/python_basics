def fibn(a,b):
    n=int(input("enter limit:"))
    for s in range(0,n):
        s=a+b
        a=b
        b=s
        print(s)
fibn(0,1)

    
    
    