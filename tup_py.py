m_tup=("mouse,[8,4,6],(1,2,3)")
m_tup=3,4.6,'dog'
print(type(m_tup))
print(m_tup)
a,b,c=m_tup
print(a)
print(b)
print(c)
s=("hello")#while holding single element it takes as string
print(type(s))
s=("hello",)
s=(type(s))
print(s)
s="hello",
print(s)
print(type(s))
n=("mouse",[8,4,6],(1,2,3))#nested index
print(n[0][3])#nested address through multi-index
print(n[1][1])
n[1][2]=5#list inside the tuple will be mutable
print(n[1][2])