# kerala vehicle number validation
# state code 2
# district code 2
# vehicle code 2 letters & 4 numbers

#eg: KL 13 AZ4457

import re
r=input("enter vehicle number")
x='^[K][L]\d{2}[A-Z]{2}[0-9]{4}$'
vehicle=re.fullmatch(x,r)
if vehicle is not None:
    print("valid vehicle number")
else:
    print("invalid vehicle number")
