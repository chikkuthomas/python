# find prime numbers between min and max and then find their sum
#interview
min=int(input("enter the min limit"))
max=int(input("enter the max limit"))
sum=0
for i in range(min,max+1):
    if(i>1):              #no need of bracket
        for j in range(2,i):  #not all if will have else
            if(i%j==0):
                break
        else:
            sum=sum+i
print(sum)
