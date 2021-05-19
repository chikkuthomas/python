#add elements from a list to odd,even,and prime list
listt=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in listt:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("even list",even)
print("odd list",odd)