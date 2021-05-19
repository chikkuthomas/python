#read numbers and find sum of n numbers
# num=int(input("enter number"))
# i=1
# while(i<=num):
#     sum=(i*(i+1))/2
#     i+=1
# print(sum)


num=int(input("enter number"))
i=1
sum=0
while(i<=num): #1<=6  2<=6 3<=6 4<=6
    sum=sum+i  #0+1=1 1+2=3 3+3=6
    i+=1
print(sum)

