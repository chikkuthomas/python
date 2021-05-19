# this considers only strings ,not numbers
import re
n='56kg'
x='\d*\w*'

match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

# # OTHER WAY #
# n='56kg'
# x='\[0-9]{2}[a-z]{2}'  # checking whether digits from (0-9)and also 2 alphabets from a-z is also satisfied
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
