a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
print(a>b)
print(b<a) 
print("and:",a>b and b<a)
print("or:",a>b or b<a)
print("not:",not 1)
print("precedence:",not a>b and a>b)
cond1=a==b
cond2=b<a
print("exp or:",cond1 or cond2)
print("const or:",-7 or 3)
print("boolean or:",5 or True)
print("negative or:",-9 or -5)
print("zero ",{} or [])
print("integer ", 2+5j or 0+0j)
print("exp and:",cond1 and cond2)
print("const and:",-7 and 3)
print("boolean and:",5 and True)
print("negative and:",-9 and -5)
print("neg 0 and ",{} and [])
print("integer and ", 2+5j and 7+7j)





