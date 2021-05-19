listt=[1,2,3,4,5,6,7,8,9]
prime=[]
nonprime=[]
for i in listt:
    if i>1:   #always give this
        for j in (2,i):
            if(i%2)==0:
                nonprime.append(i)
                break
        else:
            prime.append(i)
print("prime list",prime)
print("non prime list",nonprime)
