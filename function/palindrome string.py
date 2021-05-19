a=input("enter the string")
b=a[::-1]
if(b==a):         #comparing the orginal string with the reversed string
    print(a,"is a palindrome")
else:
    print(a,"not a palindrome")
