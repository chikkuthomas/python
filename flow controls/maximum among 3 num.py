#read 3 numbers and find the highest
num1=int(input("enter 1st number"))  #10
num2=int(input("enter 2nd number"))  #20
num3=int(input("enter 3rd number"))  #30
# if(num1>num2)&(num1>num3): #10<20 #10<30, you can also "and"
#     print("num1 is highest")
# elif(num2>num3): #20<30
#     print("num2 is highest")
# else:
#     print("num3 is highest") #30 is highest

# same program in another way
if(num1>num2): #10<20 #10<30, you can also "and"
   if(num1>num3):
    print("num1 is highest")
elif(num2>num3): #20<30
    print("num2 is highest")
else:
    print("num3 is highest") #30 is highest