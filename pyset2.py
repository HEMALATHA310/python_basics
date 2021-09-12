m={1,2,3,4}
print(m)
m.discard(4)# m.discard(4,2)
#TypeError: discard() takes exactly one argument (2 given)
print(m)
m.remove(2)
print(m)
#m.remove(2)#KeyError: 2
#print(m)
m.discard(2)
print(m)
#POP AND CLEAR
s=set("hello")
print(s.pop())
#print(s.pop(1))#TypeError: pop() takes no arguments (1 given)
print(s)
s.pop()
print(s)
s.clear()
print(s)#set will not be del just cleared
#UNION-IT gets arranged in sequence without duplicates since commutative
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A|B)
d=A.union(B)
print(d)
e=B.union(A)
print(e)
#INTERSECTION
C={1,2,3,4,5}
D={4,5,6,7,8}
print(C&D)
F=C.intersection(D)
print(F)
G=D.intersection(C)
#DIFFERNCE
X={1,2,3,4,5}
Y={4,5,6,7,8}
print(X-Y)
q=X.difference(Y)
print(q)
r=Y.difference(X)
print(r)
#SYMENTRIC
Z={1,2,3,4,5}
P={4,5,6,7,8}
print(Z^P)
u=Z.symmetric_difference(P)
print(u)
v=P.symmetric_difference(Z)
print(v)

print(G)
