print((1,2,3)+(4,5,6))
print(("7")*3)
tup=('h','e','m','a')
#del tup[1]#TypeError: 'tuple' object doesn't support item deletion
print(tup)
del tup
print(tup)#entire tuple can be deleted then we get [NameError: name 'tup' is not defined]
