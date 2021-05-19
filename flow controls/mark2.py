# num1=int(input("classes of held"))
# num2=int(input("number of classes attended"))
# num3=num2/num1  #can also use((num2/num1)*100)
# perc=num3*100
# if(perc>=75):
#     print("allowed in exam")
# else:
#     print("not allowed in exam")

# IN OTHER WAY

num1=int(input("classes of held"))
num2=int(input("number of classes attended"))
perc=(num2/num1)*100
print("PERCENTAGE OF ATTENDENCE OF THE STUDENT IS",perc)
if (perc >= 75):
    print("allowed in exam")
else:
    print("not allowed in exam")
