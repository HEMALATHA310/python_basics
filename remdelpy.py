m=['p','r','o','b','l','e','m']
del m[2]
print(m)
del m[1:5]
print(m)
v=['p','r','o','b','l','e','m']
v.remove('p')#TypeError: remove() takes exactly one argument (0 given)....if element not mentioned
print(v)
print(v.pop(1))
print(v)
print(v.pop())
print(v)
print(v.clear())