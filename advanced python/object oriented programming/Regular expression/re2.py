import re

count=0
# finditer is a method in re package
matcher=re.finditer("ab","abaabbab")# find iter is used to iterate & check first strng is in second strg
# print(matcher)
for match in matcher:
    count+=1
print("count= ", count)