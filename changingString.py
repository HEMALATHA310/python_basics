s="hema"
#s[1]='o'TypeError: 'str' object does not support item assignment
print(s)
s="python"
print(s)#str doesnt support element change but total string can be changed.
#del s[1]#TypeError: 'str' object doesn't support item deletion
print(s)
#del s
print(s)
str1='hello'
str2='world'
print('str1+str2',str1+str2)
#print('str1*3',str*3)
st=('hello'
    'world')
print(st)
a='hello"world!'
print(a)
b='hello world!'
print(b)
str3='cold'
list_enumerate=list(enumerate(str3))
print('list_enumerate(str3)',list_enumerate)
print('len(str3)=',len(str3))
#print("he said," what's there?"") #SyntaxError: invalid syntax
#print('he said," what's there?"') #SyntaxError: invalid syntax
print('''he said," what's there?''')#escape by single qoutes
print('he said," what\'s there?"')#escape by backslash
print("he said,\" what's there?\"")#incase i use double slash #use backslash# were needed. to escape this 
print("C:\\Python32\\Lib")
print("This is printed\nin two lines")
print("this is\x48 \x45\x58 representation")
print("this is\x48 representation")