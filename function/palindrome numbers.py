n=int(input("enter the number"))  #121
temp=n
pal=0
while(temp>0):
    digit=temp%10
    pal=(pal*10)+digit
    temp=temp//10
if(pal==n):
    print(n,"is a palindrome")
else:
    print("not a palindrome")
