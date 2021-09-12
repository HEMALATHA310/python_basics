y=(input("enter the string:"))#user's choice
s=""#empty string to store reverse string
for i in y:#for iterating the string characters
    print(i)
    s=i+s#it includes i value in string repeatedly till loop ends
print("the reversed string is:",s)
#method 2
a=(input("enter the string:"))
s=a[::-1]
print(s)
#method3
s=(input("enter the string:"))#user#empty string to store reverse string
for i in s:#for iterating the string characters
    s=i+s#it includes i value in string repeatedly till loop ends
half = len(s)/2#"len"is in-built where data type cannot be changed thus assigned to variable
print("the reversed string is:",s[0:int(half)])#indices to access half of the string
#here we convert data type because if don't convert and proceed directly like
#"print("the reversed string is:",s[0:(half)])"
#we get (TypeError: slice indices must be integers or None or have an __index__ method)
