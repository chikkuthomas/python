import re
lst=[]
f=open("phone","r")
for i in f: # to iterate each the file content
    d=i.rstrip("\n") #to stripout th "\n"
    lst.append(d)  # after stripping to add elements to the list

for j in lst: # to iterate each element in list and check
    x='^[+][9][1]\d{10}'
    ph=re.fullmatch(x,j) # matching each element with x
    if ph is not None:   #if matching
        w=open("num.txt","a") #here append is used since we need to add all

        w.write(j)
        w.write("\n") # to print in next line
