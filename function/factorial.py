#to find factorial of a number
# 5!=5*4*3*2*1
# 0!=1
def factorial(n):
    fact=1
    if(n<0):
        print("sorry no factorial for negative numbers")
    elif(n==0):
        print("factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            fact=fact*i
        print("factorial of ",n,"is",fact)
factorial()






