# num1=int(input("enter the first number"))
# num2=int(input("enter the second number")) # if num2=0,then there will be error in the output
# print(num1/num2)                           #hence we need exception handelling

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
try:                             # try block
    print(num1/num2)
except:                          #exception block
    print("exception occured")

#try ,except and finally blocks work together in python programming and not in any other programming languages

#try block always work irrespective of the exception