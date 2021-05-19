# read avalue and find its multiplication table
# 1*2=2
# 2*2=4
# 3*2=6
# 4*2=8

num=int(input("enter the number"))
i=1
while(i<=10):
    res=i*num      #always give inside the while loop only
    print(i,"*",num,"=",res)
    i+=1