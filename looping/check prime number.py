#check the given number is prime or not
num=int(input("enter the number"))
flag=0             #to avoid repetiton
for i in range(2,num):
    if(num%i==0):
        flag=1   #if condition is true
if(flag>0):
        print(num, "is not a prime number")
else:
    print(num,"is a prime number")
