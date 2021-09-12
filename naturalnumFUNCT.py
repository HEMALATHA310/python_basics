def nat(num):
    s=0
    for i in range(1,num+1):
        s=s+i
    print("the sum of n natural no.s are:",s)
num=int(input("enter no:"))
nat(num)