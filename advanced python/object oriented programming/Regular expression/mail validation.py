# validate a mail id
#gmail can be uppercase also
#\. means a "." will come
import re
r=input("enter the email id")
x='^[a-z0-9]+@\w+[.][c][o][m]$'
email=re.fullmatch(x,r)
if email is not None:
    print("valid email")
else:
    print("invalid email")