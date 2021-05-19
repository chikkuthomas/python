#to count th number of vowels in a string
# a=input("enter the string")
# count=0
# for i in a:
#     if i in ('a','e','i','o','u'):
#         count+=1
# print(count)
#......................................................................................................................
a=input("enter the string")
b="aeiou"
count=0
for i in a:
    if i in b:
        count+=1
print("number of vowels=",count)
