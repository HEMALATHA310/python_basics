a=(input("enter the string:"))
s=""
for i in a:
    s=i+s
if(s==a):#including reverse condition and checking i/p and reverse
    print("the given string is palindrome")
else:
    print("the given string is not a palindrome:")