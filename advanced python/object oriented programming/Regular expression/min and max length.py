#string with minimum length 8 and max length 15,numbers not allowed
import re
r=input("enter the string")
x='\D{8,15}'         #since symbols and letters are allowed,use \D
f=re.fullmatch(x,r)
if f is not None:
    print("correct")
else:
    print("false")

# we use $ to specify the rule ends there, or rule stops after that