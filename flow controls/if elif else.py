#print positive or negative else zero
num=int(input("enter the number"))
if(num>0):
    print(num,"is positive") #0>0 false, 0<0 false
elif(num == 0): #(num<0) negative this condition can also be given
    print(num, "is zero")
else:
    print(num,"is negative")


