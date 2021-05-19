# num=int(input("enter the number")) #num=153=1*1*1+ 5*5*5 + 3*3*3
# ams=0
# temp=num
# while(temp>0):
#     digit=temp%10
#     ams=(digit*digit*digit)+ams  #digit**3=raise to 3
#     temp=temp//10                #here number is given as temp bcs we are comparing the orginal number with result
# if(ams==num):
#     print(num,"is an amstrong number")
# else:
#     print(num,"not an amstrong number")

def ams(num):
    ams = 0
    temp = num
    while (temp > 0):
        digit = temp % 10
        ams = (digit * digit * digit) + ams  # digit**3=raise to 3
        temp = temp // 10  # here number is given as temp bcs we are comparing the orginal number with result
    if (ams == num):
        print(num, "is an amstrong number")
    else:
        print(num, "not an amstrong number")
ams(153)
