#starting with 'a' and ending with 'b', in btwn anything can come
import re
r=input("enter the string")
x='^a[a-zA-Z0-9\W]*b$'
f=re.fullmatch(x,r)
if f is not None:
    print("valid")
else:
    print("invalid")