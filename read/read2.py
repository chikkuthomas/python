#read two numbers from console, first num1 then num 2 and add these numbers and print two numbers

num1=int(input("enter number1"))
num2=int(input("enter number2"))
print(num1,num2)
sum=num1+num2
print("sum is equal to",sum)       #the op from console will be read as a string so we need to pass it as int before we use that number for further mathematical operation
