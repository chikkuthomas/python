# bonus of 5% if year of service is more than 5 years
# read salary and year of service and print the net bonus amount

# sal=int(input("enter your salary"))
# servc=int(input("enter the number of years of service"))
# if(servc>=5):
#     bonus=((sal*5)/100)*12
#     print(" congrats you have bonus!!!! and your bonus is",bonus,"Rs")
# else:
#     print(" sorry you have no bonus")

#HOME WORK 2
# READ YEAR, MONTH,DATE
# THEN READ UR BIRTH YEAR,BIRTH DATE,BIRTH MONTH AND FIND AGE
#
# d1=int(input("enter ur day of birth"))
# m1=int(input("enter ur month of birth"))
# y1=int(input("enter ur year of birth"))
# print("date of birth is",d1,"/",m1,"/",y1)
# d2=int(input("enter today's day"))
# m2=int(input("enter this month"))
# y2=int(input("enter this year"))
# if(m1>m2):
#    m=m2+(12-m1)
# else:
#     m=m2-m1
# if(m1>m2):
#    y=y2-y1-1
# else:
#     y=y2-y1
# if(d2>d1):
#    d=d2-d1
# else:
#     d=d1-d2
# print("your are",y,"years old")


#read a limit and print the prime numbers from 1 to that limit

#number should be greater than 1

# lim=int(input("enter limit"))   # to enter till which number we have to check
# for i in range(1,lim+1):        # start from 1 to the limit, u can also use 2 bcs 1 is not a prime number
#   if i>1:                       # do only if i ia greater than 1
#     for j in range(2,i):        #range for j
#         if(i%j==0):             #if remainder is 0,then break the program,else print i as the prime number
#             break
#     else:
#         print(i)

# lim=int(input("enter limit"))
#
# for i in range(1,lim+1):
#   if (i>1):
#     for j in range(2,i):
#         if(i%j==0):
#            break
#     else:
#         print(i)

#         *
#      *  *
#     * * *
#   * * * *
# * * * * *


# def pattern(n):
#     for i in range(0,n):
#         for j in range(n-i,0,-1):
#             print("*",end=" ")
#         print()
# pattern(5)

# count the number of l in hello
# count=0
# a=input("enter the word")
# for val in a:
#     if(val=="l"):
#         count=count+1
# print("count of l =",count)
#.......................................................................................................................
# def count(n):
#     count=0
#     for val in n:
#         if(val=="l"):
#             count=count+1
#     print("count of l =",count)
# count("lilly")
#.......................................................................................................................
#count value 0f the letter we give
# def count(n):
#     count=0
#     for val in "hello":
#         if val==n:
#             count=count+1
#     print("count =",count)
# count("o")
#.......................................................................................................................
# a=input("enter strg")
# b=input("enter element to count")
# count=0
# for i in a:      #for i in is used to iterate
#     if i in b:
#      count=count+1
# print("count is",count)

#.......................................................................................................................












