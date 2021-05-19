#to remove symbols from a string
str=input("enter the string")
b="!@#$%^&*()_+/*-><.,?':;{[]}"
c=""          #an empty string is created because we need to add the corrected string alone
for i in str:
    if i not in b:
        c+=i  # moving the string without symbols to new string

print(c)
