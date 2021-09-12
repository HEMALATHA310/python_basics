a={}#will not create an empty set
print(type(a))
a=set()
print(type(a))
#s={1,2,[3,4]}#TypeError: unhashable type: 'list'
s=set([1,2,3,2])
se={1,3}
se.add(2)#o/p:{1, 2, 3}
se.add(4)#o/p:{1,2, 3, 4}#arranges in sequence
#se.add(4,5)#TypeError: add() takes exactly one argument (2 given)
se.add(3)#o/p:{1,2, 3,4}#don't allow duplicates
print(se)
se.update([2,3,4])
print(se)
se.update([4,5],{1,6,8})#TypeError: 'int' object is not iterable
print(se)