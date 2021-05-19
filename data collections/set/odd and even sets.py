#to add odd and even eleemnts to different set
s={1,2,3,4,5,6,7,8,9}
even=set()
odd=set()
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print("even set",even)
print("odd set",odd)

