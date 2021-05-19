#cobination of lower case and upper case letters ending with number

import re
r=input("enter the string")
x='[a-zA-Z]+[0-9]$'
match=re.fullmatch(x,r)
if match is not None:
    print("valid")
else:
    print("invalid")