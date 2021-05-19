# read 3 numbers from console and find the second largest element
#100 #80  #50
#80 100 50
#100 50 80

# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# num3=int(input("enter num3"))
# if(num1>num2>num3):
#     print(num2,"is second highest")
# elif(num2>num1>num3):
#     print(num1,"is second highest")
#  else:
#     print(num3,"is the second highest")

# or  in another way NESTED IF
num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print(num2,"second highest")
    else:
         print(num3,"second largest")
elif(num2>num3)&(num2>num1):
    if(num1>num3):
        print(num1,"second highest")
    else:
        print(num3,"is second highest")
elif(num3>num1)&(num3>num2):
     if(num1>num2):
        print(num1,"is second highest")
     else:
        print(num2,"is second highest")