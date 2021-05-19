import re

n='hello'
x='\w*'
match=re.fullmatch(x,n)
if match is not None:   #to check whole a string
    print("valid")
else:
    print("invalid")