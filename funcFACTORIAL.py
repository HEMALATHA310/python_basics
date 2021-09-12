def calc_fac(x):
    """this is a recursive function"""
    if x==1:
        return 1
    else:
        return(x*calc_fac(x-1))
num=4
print("the factorial",num," is",calc_fac(num))