# read 4 subject marks

# total

#180-200 A+
# 159-179  A
# 148-158  B+
# 128-139  B
# 100-138  C+
# 80- 99   C
# 60-79    D+
#
# FAIL

mark1=int(input("enter mark1"))
mark2=int(input("enter mark2"))
mark3=int(input("enter mark3"))
mark4=int(input("enter mark4"))
total=mark1+mark2+mark3+mark4
if(total>=180)&(total<=200):
    print("A+")
elif(total>=159)&(total<=179):
    print("A")
elif(total>=140)&(total<=159):
    print("B+")
elif(total>=128)&(total<=139):
    print("B")
elif(total>=100)&(total<=119):
    print("C+")
elif(88<=total<=99):
    print("C")
elif(60<=total<=79):
    print("D+")
else:
    print("FAIL")


