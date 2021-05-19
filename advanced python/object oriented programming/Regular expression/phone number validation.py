import re
n=input("enter the phone number")
x='[+][9][1]\d{10}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid phone number")
else:
    print("not a valid a phone number")
