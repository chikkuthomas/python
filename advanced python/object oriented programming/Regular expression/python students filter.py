#filter python student id  from text file and copy it to another file
#rfc
# import re
# l=[]
# f=open("ref","r")
# for i in f:
#     d=i.rstrip("\n")
#     l.append(d)
# print(l)
# for i in l:
#     x='^[L][U][M]\d{2}[P][Y]\d{3}'
#     match=re.fullmatch(x,i)
#     if match is not None:
#         w=open("rfc.txt","a")
#         w.write(i)
#         w.write("\n")

# import re
# f2=open("rfc.txt","w")
# rule='[L][U][M]\d{2}[P][Y]\d{3}'
# f=open("ref","r")
# for num in f:
#     number=num.rstrip("\n")
#     match=re.fullmatch(rule,number)
#     if match is not None:
#
#         f2.write(number)
#         f2.write("\n")

import re
f=open("ref","r")
w=open("rfc.txt","w")
rule='[L][U][M]\d{2}[P][Y]\d{3}'

for i in f:
    l=i.rstrip("\n")
    match=re.fullmatch(rule,l)
    if match!=None:
        w.write(l)
        w.write("\n")


















