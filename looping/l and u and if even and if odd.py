#add even and add odd numbers separately
low=int(input("enter lower limit"))
up=int(input("enter upper limit"))
sum1=0
sum2=0
for i in range(low,up+1):
     if(i%2==0): #always remember to add ==
        sum1=sum1+i
     else:
       sum2=sum2+i
print("even sum",sum1) #print outside the loop
print("odd sum",sum2)