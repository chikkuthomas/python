import re
count=0
matcher=re.finditer('ab','abaabbab')
for match in matcher:
    print("match avaiable at",match.start())  #to return at which positions strng is present
    print("group",match.group())              # the string of which match is checked
    count+=1
print("count= ",count)
print()

#ab in "abaabbab" -1st position = 0
# group - ab is the string which is compared
#ab in "abaabbab" -2st position = 3
#ab in "abaabbab" -3st position = 6