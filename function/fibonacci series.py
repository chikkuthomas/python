#fibonacci series      #recursion is where a function call itself
n=int(input("enter the number"))      #n=4
n1=0                                  #n1=0
n2=1                                 #n2=1
print(n1)                            #0
print(n2)                            #1
for i in range(0,n+1):               #i=0       1       2        3         4
    n3=n1+n2                         #n3=0+1=1  1+1=2   1+2=3    2+3=5     3+5=8
    n1=n2                            #n1=1      =1      =2       =3        =5
    n2=n3                            #n2=1      =2      =3       =5        =8
    print(n3)            # 0    1     1         2        3       5         8



