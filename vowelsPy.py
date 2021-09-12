n=input("enter the string to count vowels:")
v=('a','e','i','o','u')
c=0
for i in n:
        if i not in v:
            print('''the string doesn't contain any vowel''')
            break
        else:
            c=c+1
print("count of vowels in given string is:",c)

