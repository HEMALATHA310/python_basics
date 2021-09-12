n=int(input("enter the number to be checked:"))
if(n==0):
    print("neither prime nor composite")
if(n==1):
    print("neither prime nor composite")
if(n>1):
    for i in range(2,n):
        if(n%i==0):
            print("not a prime")
            break
    else:
        print("prime")
        #if your input is 2 and u get 2%2==0 it consider to be not a prime but 2 is prime and 