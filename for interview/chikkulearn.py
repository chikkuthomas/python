# set of rules
# while defining a variable
# 1 never start a identifier with a number
# eg 1num=10 is not allowed
#........................................................................................................................
# u can add any alphabet in front of a variable
# for eg Anum=10
#........................................................................................................................
# u can use _ in front of a variable
# eg _num=10
#........................................................................................................................
# you can have any size for your variable
#     eg numnumnumnumnumnumnum=10
#........................................................................................................................
#     don't keep space before a variable
#........................................................................................................................
#  always use standard variable names
# eg a=1 is not standard nut num1=10 is standard
#
#  while defining a variable
# Num=10
# num=10
# NUM=10
# all these are considerd as different variables
#........................................................................................................................
# use " " whenever we represent a string or a chara
#........................................................................................................................
# revision
#
# how to print hello
#
# print('hello')      #because here hello is a string
#
# # always remember python is a dynamic language so whatever comes last is accepted by it
#
# #print my name is chikku and i live in kannur
#
# name="Chikku"
# loc="kannur"               #always use " ' for names
# print("my name is",name,"and I live in",loc)
#........................................................................................................................

# to swap two numbers without using print application
# num1=10
# num2=20
# print("before swapping")
# print(num1)
# print(num2)
# temp=num1        #here we are allocating memory temporarly
# num1=num2
# num2=temp
# print("After swapping")
# print("num1=",num1)
# print("num2=",num2)
#........................................................................................................................
# swap numbers using operators
# num1=num1+num2  #10+20=30
# num2=num1-num2  #30-20=10
# num1=num1-num2    #30-10=20  #here since python is a dynamic language only the last will be considered
# print ("after swapping","num1=",num1,"num2=",num2)
#........................................................................................................................
# basic knowledge
# 5trending languages

#5 C# (c sharp) developed by microsoft used in windows
# framework is .net, mvc

# 4 java
# ide: eclipse, Netbeans, intelligie
# framework : spring,spring boot,hibernation


# 4 python
# used mainly in web development, big data analysis,  data science
# and also in machine learning,game development,artificial intelligence

# big data analysis where high velocity high capacity files are fetched and crossed
# spack python

# data science to predict future using the existing data or results

# ide for python: pycharm, jupiter notebook, spyder, anaconda
# framework: django, flask

# 3 JAVASCRIPT
# used in web page development
#    static webpage eg wikipedia
#    dynamic webpage which changes each second eg cricket score, weather (javascript is mainly used here)

# ide for javascript visual studio,netbeans, atom
#     framework angular, react, nodejs, polymer
#
# 2 RUST programming language for  mozilla firefox
#
# 2 GOOLANG developed by google
#
#
# 1 DART trending no1 is used to develop an android and ios application at the same time
# framework used is FLUTTER
#........................................................................................................................
# DIFFERENT TYPES OF PROGRAMMING LANGUAGES
# 1 object oriented programming
# 2 procedural
# 3 scripting
# 4 client side
# 5 server side
# 6 strictly typed
# 7 dynamic typed
# 8 static typed programming languages

# static typed
# eg int a;    datatype of the variable name
#    a=10;     value for the variable name
#
#  dynamic typed
#  a=10   variable name= value
# a="chikku"   here the variable is read as a name
#
# in static type once the variable is defined then again onwards that variable can be used for that data type only
# var a;   not defined
# a=30;    again onwards a can take only integier values
# a=50;    accepted
# a="chikku"; is not accepted
#
# eg for dynamic type is PYTHON
#
#     IN PYTHON WE USE COLLECTIONS because here heterogenous data can be stored

#........................................................................................................................
# to read ur age,name and qualification

# name=input("enter ur name")
# age=input("enter ur age")
# qual=input("enter ur qualification")
# print(name,age,qual)

# to read two numbers from console and add these numbers
# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# sum=num1+num2
# print("sum =",sum)
#........................................................................................................................
# OPERATORS
#
# COMPOUND ASSIGNMENT OPERATORS
# *,+,-,/,**,//,%

# num=50
# num+=2     #num=50+2
# print(num)  #52

# num=30
# num-=20  #30-20
# print(num)

# num=20
# num/=4
# print(num)


# a=50
# a**=4
# print(a)

# a=74
# a//=3 #to find 74/3 without the decimal
# print(a) #24 ans

# a=17
# a%=2  #to find the remainder
# print(a)

# a=8
# a*=86  #8 * 86
# print(a)  #688
#........................................................................................................................
# RELATIONAL OPERATORS
# <,>,<=,>=,!=,==
# always the output will be TRUE or FALSE
# Value of true =1, value of false =0

# num1=int(input("enter num1")) #50
# num2=int(input("enter num2")) #20
# print(num1>num2)  true
# print(num1<num2)     false
# print(num1>=num2)    true
# print(num1<=num2)      false
# print(num1==num2)       false
# print(num1!=num2)        true

#to multiply two numbers read from console
# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# mul=num1*num2
# print(mul)
#........................................................................................................................
# FLOW CONTROLS
# IF,IF ELSE, IF...ELIF....ELSE (DECISION MAKING)
# FOR, WHILE  (LOOPING)
# JUMPING(PASS,BREAK,CONTINUE)
#
# IF ELSE
# mark=int(input("enter your mark"))
# if(mark>50):
#     print("you are qualified")
# else:
#     print("you are not qualified")

# LOGICALS
# AND,OR,XOR
# XOR WHERE BOTH BITS OF NUMBERS ARE SAME THEN OP IS 0

# num1=2
# num2=3
# print(num1&num2) AND # ans is 2

# a=3
# b=5
# print(a^b) XOR #ans is 6

# num1=8
# num2=3
# print(num1|num2) #OR ans is 11

# input    &(AND)  |(OR)     ^(XOR)
# 0 0       0        0         0
# 0 1       0        1         1
# 1 0       0        1         1
# 1 1       1        1         0

# BINARY NUMBERS
# 0  0000
# 1  0001
# 2  0010
# 3  0011
# 4  0100
# 5  0101
# 6  0111
# 7  1000
# 8  1001
# 9  1010
# 10 1011
#........................................................................................................................
# find whether numbers are odd or even
# num=int(input("enter num"))
# if(num%2==0):
#     print("number is even")
# else:
#     print("number is odd")

#........................................................................................................................
#find the max among two numbers
# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# if(num1>num2):
#     print("num1 is highest")
# else:
#     print("num2 is highest")
#........................................................................................................................
#maximum amomg three numbers

# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# num3=int(input("enter num3"))
# if(num1>num2)&(num1>num3):
#     print(num1,"is highest")
# elif(num2>num3):
#     print(num2,"is highest")
# else:
#     print(num3,"is highest")

#........................................................................................................................
#find if number is highest or whether both numbers are equal

# num1=int(input("enter num1"))
# num2=int(input("enter num2"))
# if(num1>num2):
#     print("num1 is highest")
# elif(num1<num2):
#     print("num2 is highest")
# else:
#     print("both are equal")
#........................................................................................................................
#allowed for exam

# classes=int(input("total no of classes held"))
# attended=int(input("enter the number of classes attended"))
# perc=(attended/classes)*100
# print("percentage of attendence is",perc)
# if(perc>=75):
#     print("allowed for exam")
# else:
#     print("not allowed for exam")
#........................................................................................................................
#read marks and grade them

# num1=int(input("enter mark1"))
# num2=int(input("enter mark2"))
# num3=int(input("enter mark3"))
# num4=int(input("enter mark4"))
# total=num1+num2+num3+num4
# print("total marks scored is",total)
# if(90<=total<=100):
#     print("A+")
# elif(80<=total<=89):
#     print("A")
# elif(60<=total<=79):
#     print("B+")
# elif(40<=total<=59):
#     print("C")
# elif(20<=total<=39):
#     print("C+")
# elif(10<=total<=19):
#     print("D+")
# else:
#     print("failed")
#........................................................................................................................
#check whether the number is positive or negative

# num=int(input("enter the number"))
# if(num>0):
#     print("number is positive")
# elif(num==0):
#     print("number is zero")
# else:
#     print("number is negative")
#........................................................................................................................
# num1=int(input("enter the number"))
# num2=int(input("enter the number"))
# sum=num1+num2
# print("sum=",sum)
#........................................................................................................................
# num1=int(input("enter the numbers"))
# num1*=2
# print(num1)
#........................................................................................................................
# num1=int(input("enter the numbers"))
# num2=int(input("enter the numbers"))
# print(num1>num2)
#........................................................................................................................
# age=int(input("enter your age"))
# sex=input("enter your gender")
# mar=input("enter ur marital status")
# if(sex=='f'):
#     print("you can work only in urban areas")
# elif(sex=='m')&(20<=age<40):
#     print("you can work anywhere")
# elif(sex==male)&(40<=age<60):
#     print("you can work only in urban areas")
# else:
#     print("error")
#........................................................................................................................
#find the second highest number among three numbers
# num1=int(input("enter num1"))
# num2=int(input("enter number2"))
# num3=int(input("enter number3"))
# if(num1>num2)&(num1>num3):
#     if(num2>num3):
#         print(num2,"is second highest")
#     else:
#         print(num3,"2nd highest")
# elif(num2>num1)&(num2>num3):
#     if(num1>num3):
#         print(num1,"2nd highest")
#     else:
#         print(num3,"is 2nd highest")
# elif(num3>num1)&(num3>num2):
#     if(num1>num2):
#         print(num1,"is 2nd highest")
#     else:
#         print(num2,"is 2nd highest")
#........................................................................................................................
#to print from 1 to 10
# intialisation
# condition
# statement
# increment/decrement
# i=1 #initialisation
# while(i<=10): #condition
#     print(i)  #statement
#     i+=1      #increment
#........................................................................................................................
# i=1
# while(i<=10):
#     print("hello")
#     i+=1
#........................................................................................................................
# i=10
# while(i>=0):
#     print(i)
#     i-=1
#........................................................................................................................
# lim=int(input("enter the limit"))
# i=1
# while(i<=lim):
#     print(i)
#     i+=1
#........................................................................................................................
# #multiplication table
# num=int(input("enter the number"))
# i=1
# while(i<=10):
#     mul = i * num
#     print(num,"*",i,"=",mul)
#     i+=1
#........................................................................................................................
#to program a calculator
# sel=input("select the operator")
# num=int(input("enter number"))
# num1=int(input("enter number 2"))
# if(sel=='+'):
#     print(num+num1)
# elif(sel=='-'):
#     print(num1-num)
# elif(sel=='*'):
#     print(num1*num)
# elif(sel=='/'):
#     print(num/num1)
# else:
#     print("error message")
#........................................................................................................................
#lower limit to upper limit and then print them
# low=int(input("enter lower limit"))
# up=int(input("enter upper limit"))
# while(low<=up):
#     print(low)
#     low+=1
#........................................................................................................................
#lower and upper and also only even
# low=int(input("enter lower limit"))
# up=int(input("enter upper limit"))
# while(low<=up):
#     if(low%2==0):
#         print(low)
#     low+=1
#........................................................................................................................
# #sum of n numbers
# num=int(input("enter the numbers"))
# i=1
# while(i<=num):
#      sum=(i*(i+1)/2)
#      i+=1
# print(sum)
#........................................................................................................................
# num=int(input("enter the number"))
# i=1
# sum=0
# while(i<=num):
#     sum=sum+i
#     i+=1
# print(sum)
#........................................................................................................................
#forloop
# for i in range(1,11,2):
#     print(i)
# for i in range(10,0,-1):
#     print(i)
#........................................................................................................................
#lower and upper limit using for loop
# low=int(input("enter lower limit"))
# up=int(input("enter lower limit"))
# for i in range (low,up+1):
#     print(i)
#........................................................................................................................
#reverse a number
# num=int(input("enter the number"))
# res=0
# while(num!=0):
#     digit=num%10
#     res=(res*10)+digit
#     num=num//10
# print(res)
#........................................................................................................................
# num=int(input("enter the number"))
# res=0
# while(num!=0):
#     digit=num%10
#     res=(res*10)+digit
#     num=num//10
# print(res)
#........................................................................................................................
#10 integiers from keyboard and find their average
# limit=10
# i=1
# sum=0
# while(i<=limit):
#     sum=sum+i
#     i+=1
# print("avg",sum/10)
#........................................................................................................................
##program to find numbers which are divisible by 7 which is also a multiple of 5,between 1500 & 2700
# low=1500
# up=2700
# while(low<up):
#     if(low%7==0)&(low%5==0):
#        print(low)
#     low+=1
#.......................................................................................................................

#to reverse a number
# num=int(input("enter a number"))
# res=0
# while(num!=0):
#     digit=num%10
#     res=(res*10)+digit
#     num=num//10
# print(res)
#..........................................................................................................................
#using for loop print even number from the given limit
# low=int(input("enter a lower number"))
# upp=int(input("enter upper number"))
# for i in range(low,upp+1):
#     if(i%2==0):
#        print(i,"even")
#     else:
#         print(i,"odd")
#........................................................................................................................
#to add even and odd numbers separately
# low=int(input("enter a lower number"))
# upp=int(input("enter upper number"))
# sum=0
# sum1=0
# for i in range(low,upp+1):
#     if(i%2==0):
#         sum=sum+i
#     else:
#         sum1=sum1+i
# print("even sum",sum)
# print("odd sum",sum1)
#........................................................................................................................
#to check whether the given number is prime or not
#always to find prime number, it should not be divisible by any number
# so find if the number is divisible by all the numbers from 2 to that number-1
# prime numbers are always divisible by that number and 1

# num=int(input("enter the number"))
# flag=0
# for i in range(2,num): # check whether the number is divisible by num from 2 to num-1
#     if(num%i==0):     # if remainder when divided is 0 then not prime
#         flag=1       # flag is set as 1 (true) if the condition is satisfied else flag is 0
# if(flag>0):          #flag is greater then the not prime condition is satisfied hence print
#     print(num,"is not prime")
# else:
#     print(num,"is a prime")  #if flag is zero the its a prime number
#.......................................................................................................................
#print an array
# for i in range(1,5):
#     for j in range(1,5):
#      print(j,end='')
#     print()

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=' ')
#     print()
#.......................................................................................................................
#to print
# 1
# 1 2
# 1 2 3
# for i in range(1,4):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
#.......................................................................................................................
#to find prime numbers given in a limit

# lim=int(input("enter the limit"))
# for i in range(1,lim+1):     #i=3      4        5                       2
#     if(i>1):                 #3>1      4>1      5>1                     2>1
#         for j in range(2,i): #j =2     2,3      2,3,4                   1
#             if(i%j==0):      #3%2!=0   4%2=0    5%2!=0,5%3!=0,5%4!=0
#                 break                  #break
#         else:
#             print(i)         #3                  5
#........................................................................................................................
#to find prime numbers from lower to upper limit
# low=int(input("enter the lower limit"))
# upp=int(input("enter the upper limit"))
# for i in range(low,upp+1):
#     if(i>1):
#         for j in range(2,i):
#             if(i%j==0):
#                 break
#         else:
#             print(i)
#to print in next line
# print("twinkle,twinkle,little star,\n\thow I wonder what you are")   #\n used to make it in next line...\t  is used to make space

#......................................................................................................................

# r=int(input("enter the radius"))
# area=3.14*r*r
# print("area of the circle is",area)

# first=input("enter ur first name")
# last=input("enter ur last name")
# print(last,first)

# num1=int(input("enter the num1"))
# num2=int(input("enter the num2"))
# sum=num1+num2
# print("sum =",sum)
# ........................................................................................................................
#finish the pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# for i in range(0,5):
#     for j in range(5-i,0,-1):
#          print(j,end=" ")
#     print()
# ........................................................................................................................
#we use break statement to switch the loop
# for val in "string":
#     if(val=="i"):
#         break     #here when the val =i, the loop is breaked
#     print(val)
# print("the end")
#........................................................................................................................
# for val in "chikku":
#     if(val=="h"):
#         continue #here if the condition is satisfied only that step will be skipped and rest all will be continued
#     print(val)
# ........................................................................................................................
#function without an argument
# def add():      #here add is the name of the function and we define it using def
#     a=int(input("enter number"))
#     b=int(input("enter number"))
#     print(a+b)
# add()           #always call the function outside, u can call it wherever u want
# ........................................................................................................................
#function with argument
# def add(a,b):        #here already parameters are given
#     print(a+b)
# add(7,8)           # so while calling use the parameters too

#function with arguments and return types
# def add(a,b):
#     return(a+b)
# print(add(3,7))
# ........................................................................................................................
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# for i in range(1,6):        #1  2    3      4          5
#      for j in range(1,i+1): #1  1 2  1 2 3   1 2 3 4   1 2 3 4 5
#          print('*',end=" ")   #1  2 2  3 3 3   4 4 4 4   5 5 5 5 5
#      print()
# ........................................................................................................................
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

#........................................................................................................................
# def present():
#     a=input("enter the letter")
#     for val in "luminar":
#         if(val in a):
#            print("present")
#            break
#         else:
#            print("not present")
#            break
# present()

#.......................................................................................................................
#to print a triangular pattern
# def pattern(n):

#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             print(end=" ")
#         n=n-1
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# pattern(11)
#.......................................................................................................................

#to find the factorial of a number
# def factorial(n):
#     fact=1
#     if (n==0):
#         print("factorial of 0= 1")
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# factorial(8)
#.......................................................................................................................
#to check present or not present
# def present():
#     flag=0
#     a=input("enter the string")
#     for val in ("string"):
#         if a in val:
#             flag=1
#     if (flag>0):
#         print("present")
#     else:
#         print("not present")
# present()
#.......................................................................................................................
#print common
# def common(a):
#     flag=0
#     for b in "chikku":
#         if a in b:
#           flag=1
#     if(flag>0):
#         print("same")
# common("n")
#.......................................................................................................................
#calculator
# def add(a,b):
#     return(a+b)
# def sub(a,b):
#     return(a-b)
# def mul(a,b):
#     return(a*b)
# def div(a,b):
#     return(a/b)
#
# print("select operator")
# print("1.add")
# print("2.sub")
# print("3.mul")
# print("4.div")
# while True:
#     choice=input("enter choice")
#     if choice in ('1','2','3','4'):
#         c=float(input("enter num"))
#         d = float(input("enter num"))
#         if choice=='1':
#             print(add(c,d))
#         elif choice == '2':
#               print(sub(c,d))
#         elif choice == '3':
#               print(sub(c,d))
#         elif choice == '4':
#               print(div(c,d))
#         else:
#             print("invalid")
#.......................................................................................................................
#to print a calculator
# def add(a,b):
#     return(a+b)
# def sub(a,b):
#     return(a-b)
# def mul(a,b):
#     return(a*b)
# def div(a,b):
#     return(a/b)
# print("select the operators")
# print("1.add")
# print("2.sub")
# print("3.mul")
# print("4.div")
# while True:
#     choice=input("enter the choice")
#     if choice in ('1','2','3','4'):
#         a=float(input("enter the number"))
#         b = float(input("enter the number"))
#         if(choice=='1'):
#             print(add(a,b))
#         elif (choice == '2'):
#             print(sub(a, b))
#         elif(choice=='3'):
#             print(mul(a,b))
#         elif(choice=='4'):
#             print(div(a,b))
#         break
#     else:
#         print("invalid")
#..................................................................................................................

#factorial of numbers
# def factorial(n):
#     fact=1
#     if(n<0):
#         print("sorry no factorial for negative numbers")
#     for i in range(1,n+1):  #here since the value is starting from 1, the value when n=0, will be printed as the initial value of fact
#         fact=fact*i
#
#     print("factorial of",n,"=",fact)
# factorial(4)
#.....................................................................................................................

#how to swap the content in a to b without using swap
# a=input("enter the string")
# b=""
# for i in a:
#     if i not in b: # comparing each string with that of string in b,if i!=b,then
#         b+=i  #the b is added with elements in i
# print(b)     #always use if i in or if i not in instead of (i==b),because it won't work always

#.......................................................................................................................

#how to remove symbols from a string

# a=input("enter the string")
# b="!@#$%^&*()_+*-/<>,.:;\|{}[]"
# c=""
# for i in a:
#     if i not in b:
#         c+=i
# print(c)
#.......................................................................................................................
# fibonacci series
# n=int(input("enter the number"))
# n1=0
# n2=1
# print(n1)
# print(n2)
# n3=0
# for i in range(0,n):
#         n3=n1+n2
#         n1=n2
#         n2=n3
#         print(n3)

#.......................................................................................................................
# #fibonacci series using recurssion
# def fibo(n):                   #n=4
#     if(n<=1):                  #4>1
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2) #fibo(3)+fibo(2)
# n=int(input("enter the number"))    # actual program starts here
# if n<=0:                            #n>0
#     print("please enter positive integer")
# else:
#     print("fibonacci series:")     #fibonacci series
#     for i in range (n):            #(0,4)
#         print(fibo(i))             #print(fibo(4))
#.......................................................................................................................
#amstrong number
# num=int(input("enter the number"))
# ams=0
# temp=num
# while(temp>0):
#     digit=temp%10
#     ams=(digit**3)+ams
#     temp=temp//10
# if(ams==num):
#     print(num,"is an amstrong number")
#
# else:
#     print(num,"is not an amstrong number")

#.......................................................................................................................
#palindrome

# a=input("enter the word")
# b=a[::-1]
# if(b==a):
#     print(a,"is a palindrome")
# else:
#     print(a,"is not a palindrome")

#.......................................................................................................................
# #intrv pattern
# 1
# 11
# 111
# 222
# 22
# 2
# 3
# 33
# 333
# 444
# 44
# 4
# l=int(input("enter the initial range"))
# n=int(input("enter the final range"))
# for i in range(l,n):
#     if(i%2!=0):
#         r=6
#         for k in range(0,r):
#             for j in range(0,k+1):
#                 print(i,end="")
#             print()
#     else:
#         r1=6
#         for k in range(0,r1):
#             for j in range(r1-k,0,-1):
#                 print(i,end="")
#             print()
#.......................................................................................................................

# s={1,2,3,4}
# print(s)
# print(type(s))

# s=set()
# print(s)
# s.add("chikku")
# s.add(3)
# s.add(9.2)
# s.add(True)
# print(s)
#.......................................................................................................................

#to input elements into an empty set
# s=set()
# lim=int(input("enter the limits"))
# for i in range(1,lim+1):
#     ele=input("enter the elements")
#     s.add(ele)
# print(s)
#.......................................................................................................................

#to convert temp to C and Farenheit

# print("the temperature medium")
# print("c for celcius")
# print("f for farenhiet")
# while True:
#     choose=input("choose the medium")
#     if choose in('c','f'):
#         temp = float(input("enter the temp"))
#         if choose=="c":
#             tempf=((9/5)*temp)+32
#             print("temperature in farenheit is",tempf,"F")
#             break
#         elif choose=="f":
#             tempc=(5/9)*(temp-32)
#             print("temperature in degree celcius is",tempc,"C")
#             break
#     else:
#         print("invalid")
#         break
#......................................................................................................................
 #using nested for loop, print following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# i=int(input("enter the initial range"))
# n=int(input("enter the final range"))
# for i in range(i,n+1):
#     if(i%2!=0):
#         r=5
#         for k in range(0,r):
#             for j in range(0,k+1):
#                 print("*",end=" ")
#             print()
#     else:
#         r1=4
#         for k in range(0,r1):
#             for j in range(r1-k,0,-1):
#                 print("*",end=" ")
#             print()
#
#
#......................................................................................................................
#to guess a number
# num=int(input("enter a number"))
# flag=0
# if (1<=num<=9):
#     flag=1
#     if(flag==1):
#         print("well guessed!")
# else:
#     print("guess more")

#....................................................................................................................
#count the number of even and odd numbers from a series of number
# ini=int(input("enter the inital range"))
# fin=int(input("enter the final range"))
# i=0
# m=0
# for k in range(ini,fin+1):
#     if(k%2==0):
#         i+=1
#     else:
#         m+=1
#
# print("number of even numbers=", i)
# print("number od odd numbers=",m)
#.....................................................................................................................
#program to print all the numbers from 0 to 6 expect 3 and 6

# for i in range(0,7):
#     if(i==3 or i==6):
#         continue
#     print(i,end=" ")
# print("")
#................................................................................................................
#for mul of 3-bizz,mul of 5-fizz,mul of 3&5- fizzbizz
# for i in range(1,51):
#      if (i % 5 == 0) & (i % 3 == 0):
#          i = "fizzbizz"
#          print(i)
#      elif(i%5==0):
#          i="fizz"
#          print(i)
#      elif(i%3==0):
#          i="bizz"
#          print(i)
#      else:
#          print(i,end=" ,")
# print()
#.................................................................................................................
#slicing of list:
# a=[1,2,3,4,5,6,7,8,9]
# print(a[-1])
# print(a[0:4])
# #to update the list:
# a[3]=34
# print(a)
#.................................................................................................................
#
# a=[1,2,3,4,5]
# b=[6,7,8,9,1,2]
# c=[]
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)
#.......................................................................................................................
# a=[1,2,3,4,5]
# b=[]
# s=1
# for i in a:
#     s=i*i
#     b.append(s)
# print(b)
#.......................................................................................................................
#form a directory, then make a python file where we are adding functions
#def add(x,y):
# print(x+y)
#from directory import file as p #this is for aliasing
# p.add(2,5)

#if we need to do only one function defined in the file
#from directory.file import add

#................................................................................................................
# a=[1,2,3]
# b=[]
# for i in range(0,3):
#     b.append(a[i])
# print(b)

#..................................................................................................................
#sorting elements of an array in ascending order without using sort -nested for loop
#Initialize array
# a = [5, 2, 8, 7, 1]
# temp = 0
#
# #Displaying elements of original array
# print("Elements of original array: ")
# for i in range(0,len(a)):        #(0,5)
#         print(a[i],end=" ")      #5 2 8 7 1
#
# #Sort the array in ascending order
# for i in range(0, len(a)):
#     for j in range(i+1, len(a)):
#         if(a[i] > a[j]):
#             temp = a[i];
#             a[i] = a[j]
#             a[j] = temp;
#
# print();
#
# #Displaying elements of the array after sorting
#
# print("Elements of array sorted in ascending order: ");
# for i in range(0, len(a)): #this is used to print every elements,otherwise only last element will be printed
#     print(a[i], end=" ")

#.......................................................................................................................
# sorting elements of a list in ascending order using while
# #
# a=[4,6,7,9,2,1,8]
# print(a)
# b=[]
# while a:
#     min=a[0]
#     for i in a:
#         if(i<min):
#             min=i
#     b.append(min)
#     a.remove(min)
# print("list after sorting=",b)

#.......................................................................................................................

# to sort using sort keyword and then find the min and max elements
# a=[5,6,4,8,1,27,93,4,1,2]
# a.sort()
# print(a)
# print("mininum element of the list=",a[0])
# print("maximum element of the list=",a[-1])

#.......................................................................................................................

# comprehension
# where the code is made simple

#to find the even elements  list from 0 to 20

# even=[i for i in range(0,21) if(i%2==0)]
# print(even)

#.......................................................................................................................

#to print squares of elments in a list

# a=[1,2,4,5]
# squares=[i**2 for i in a]
# print(squares)
#.......................................................................................................................

# binary search of list

# a=[41,5,6,84,96,2,7,12,3,1]
# def bsearch():
#     a.sort() #[1,2,3,5,6,7,12,41,84,96]
#     ele=int(input("enter the element"))
#     flag = 0
#     low=0
#     upp=len(a)-1      #10-1=9
#     while(low<=upp):
#         mid = (low + upp) // 2  #(0+90)//2=4                               mid=1                 mid=3
#         if(ele>a[mid]):         # ele=5,a[4]=6,5!>6, false exit loop       5>2,true              5>3,true
#             low=mid+1                                                    #  low=1+1=2 ,a[2]=3    low=2+1=3,a[3]=5
#         elif(ele<a[mid]):      # 5<6,true                                                         5!<5, false exit loop
#             upp=mid-1          #upp=4-1=3, mid=(0+3)//2=1,a[1]=2
#         elif(ele==a[mid]):    # 5!=6, exit loop                                                    5==5, true
#             flag=1                                                                               # flag=1
#             break                                                                    # break, since we found the element
#     if(flag==1):                                                                     # since flag==1
#         print("found")                                                               # print found
#     else:
#         print("not found")
# bsearch()

#......................................................................................................................

#dictionary

# dict={'name':'chikku','age':26,'hobby':'painting'}
# print(dict)
# dict['colour']='yellow'
# a={"size":'small'}
#
#
# dict['name']='chinchu'
# print(dict)
# #to add a dictionary to a dictionary
# dict.update({'education':'engineering'})
# print(dict)
# dict.update(a)
# print(dict)
# del dict['colour']
# print(dict)
# dict.clear()
# print(dict)
# print(type(dict))
# del dict
# print(dict)

#.......................................................................................................................
# checking key
#
# dict={'name':'chikku',"age":26,'colour':'green'}
# ele=input("enter the element")
# for i in dict:
#     if(i==ele):
#         print(ele,"present")
#         break
# else:
#     print(ele,"not present")

#.......................................................................................................................
 # checking key in a dictionary using function
# def key(x):
#      dict = {'name': 'chikku', "age": 26, 'colour': 'green'}
#      if x in dict:
#          print("present")
#      else:
#          print("not present")
# key('name')

#.......................................................................................................................

# to check the count of same string and add it to the dictionary

# dict={}
# string=input("enter the string")
# words=string.split(" ")
# for i in words:
#     if i not in dict:
#         dict.update({i:1})
#     else:
#         val=int(dict[i])
#         val+=1
#         dict.update({i:val})
# print(dict)

#........................................................................................................................

#TUPLES
#IMMUTABLE

# t=1,2,3,4,5
# len(t)
# max(t)
# min(t)
# print(max(t),min(t),len(t))
# print(t[0])
# # when a single element tuple, we need to put a "," , otherwise it is considered as an integer
# a=3,
# print(a)
# here we can nest a tuple with a list
#.......................................................................................................................

# tuples program

#to print certain tuple from a list
#here we are adding  tuples to a list
# details=[('chin',26,400000),("min",31,500000),('chik',26,400000)]
# for i in details:
#     if i[2]>=500000:
#         print("details of the employee",i)

#.......................................................................................................................

# write a python program to count the number of strings where the string length is 2 or more and the first
# # and last characters are same from a given strings
# program in string

# def count(lst):
#     count=0
#     for word in lst:
#         if len(word)>1and word[0]==word[-1]:
#             count+=1
#     return count
# print(count(['abc','cdw','aba','121']))   #ans= 2


#...........................................................................................................................
 # to multiply all elements in a list

# lst=[1,2,3,4,5,6,7]
# mul=1
# for i in lst:
#     mul=mul*i
#     print("multiples of all the elements in the list =",mul)

#.......................................................................................................................

# write a python program to get a list ,sorted in increasing order by the last element in each tuple from a given list of
# non-empty tuples
# so here we have to arrange the tuples in the ascending order of their last element
#
# a=[(2,5),(1,2),(4,4),(2,3),(2,1)]
# print("before sorting",a)
# for i in range(0,len(a)):       # (0,5)
#     for j in range(0,len(a)-i-1): #(0,5-i-1)=(0,4-i)
#         if a[j][-1]>a[j+1][-1]:    #second element of each tuple is compared here,eg:a[0][-1]=1 in (2,1)
#             temp=a[j]
#             a[j]=a[j+1]
#             a[j+1]=temp
# print("after sorting",a)
#
#     EXPLANATION     #
# when i=0, j=(0,4)
#
# checking condition for j=0
# if a[0][-1]>a[1][-1]
# a[0] and a[1] is swapped hence the new list= [(1,2),(2,5),(4,4),(2,3),(2,1)]
#
# j=1
# if a[1][-1]>a[2][-1] { 5>4} true
# hence a[1] swapped with a[2] = [(1,2),(4,4),(2,5),(2,3),(2,1)]
#
# j=2
# a[2][-1]> a[3][-1] 5>3, true
# (2,5) swapped (2,3)= [(1,2),(4,4),(2,3),(2,5),(2,1)]
#
# j=3
# condition true
# a=[(1,2),(4,4),(2,3),(2,1),(2,5)]
#
# if the condition is not true yet the j value will be incremeneted
# again if its not met, i will be incremented till len(a)


#.......................................................................................................................

#.......................................................................................................................

#to remove the duplicates from the list

# a=[1,2,3,4,5,3,6,8,6]
# print(a)
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i) -while appending to anew list it wont add the duplicate elements
# print(b)

#........................................................................................................................

# python program to create a list of tuples from given list having number and its cube in each tuple

#here we can use only inline implimentation
# i.e we can use only list comprehension

# lst=[1,2,3,4,5]
# res=[(i,i**3) for i in lst]
# print(res)

#.......................................................................................................................

# count the number of matching characters in a number of strings
# inp=input("enter the string")
# inp1=input("enter the string")
# count=0
# for i in inp:
#     if i in inp1:
#         count+=1
# print("number of matching characters=",count)

#.......................................................................................................................

# write a program to reverse each tuple in a list of tuples

# lst=[(2,1),(3,4),(5,6)]
# print("before reversing ",lst)
# b=[]
# for i in lst:       # list to iterated to get each tuple in the list
#     j=i[::-1]       # each tuple is reversed
#     b.append(j)
# print("after reversing ",b)

#.......................................................................................................................
# exam questions


# 1.Write a code in three lines to sort and eliminate duplicate elements in the list lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# lst.sort()
# b=[]
# for i in lst:
#     if i not in b:
#         b.append(i)
# print(b)

#.......................................................................................................................
# 3 line code to sort and eliminate duplicate element from the list
# a=[1,2,2,3,4,5,3,6,2]
# b=list(set(a))
# print(b)

#.......................................................................................................................
# make the text file and python file in the same directory otherwise it wont give output
# k=open("count","r")
# dict={}
# for i in k:
#     word=i.split(" ")
#     for j in word:
#         if j in word:
#             if j not in dict:
#                 dict.update({j:1})
#             else:
#                 val=int(dict[j])
#                 val+=1
#                 dict.update({j:val})

#.......................................................................................................................

# 3.Find second largest element from the list lst=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]

# lst=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
# lst.sort()
# print(lst[-2],"is the second largest element from the list")

#.......................................................................................................................

# 4.Find the common elements from the two lists a=[1,2,3,45,6,7,33,11,77,9,0,5]
# b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]

# a=[1,2,3,45,6,7,33,11,77,9,0,5]
# b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
# c=[]
# for i in a:
#     if i in b:
#         c.append(i)
# print("common elements are ",c)

#.......................................................................................................................

# to make a word count dictionary from the text file, file content is
#
# "When making changes to the source code that
# programs are made up of programmers need to make other programmers aware of the task that the routine is to perform
# They do this by inserting comments in the source code so that others can understand the program more easily and by
# documenting their code To save work programmers often use libraries of basic code that can be modified or customized
# for a specific application This approach yields more reliable and consistent programs and increases programmers
# productivity by eliminating some routine steps"

# f=open("count","r")
# dict={}
# for i in f:
#   word=i.split(" ")
#   for j in word:
#       if j not in dict:
#           dict.update({j:1})
#       else:
#           val=int(dict[j])
#           val+=1
#           dict.update({j:val})
# print(dict)

#.......................................................................................................................

#algorithm
# operations like stack eg q

#.......................................................................................................................
 # to create a stack from list:

#push -when we do this operation we can add values
#pop- you can pop out the last in the list
#display u have to display the list

# stack=[]
# top=0
# n=0
# size=int(input("enter the size "))
#
# def push():
#     global top,size
#     if top>size:
#         print("the stack is full")
#     else:
#         ele=int(input("enter the element"))
#         stack.append(ele)
#         top+=1
#
# def pop():
#     global top,size
#     if top<=0:
#         print("the stack is empty")
#     else:
#         stack.pop()
#         top-=1
# def display():
#     print(stack)
#
# while(n!=1):
#     print("choose the operation")
#     op=int(input("1)PUSH, 2)POP, 3)DISPLAY"))
#     if op==1:
#         push()
#     elif op==2:
#         pop()
#     elif op==3:
#         display()
#     n=int(input("press 1 for exist,else to continue press 2"))

#.......................................................................................................................

# To develop a queue operation:
# queue=[]
# top=0
# size=int(input("enter the size"))
# n=0
#
# def enqueue():
#     global top,size
#     if top>size:
#         print("queue is in overflow condition")
#     else:
#         p=int(input("enter the element"))
#         queue.append(p)
#         top+=1
#
# def dequeue():
#     global top, size
#     if top<=0:
#         print("queue is in the overflow condition")
#     else:
#         queue.pop()
#         top-=1
#
# def front():
#     print("first item in the queue",queue[0])
#
# def gear():
#     print("last item in the queue", queue[-1])
# def display():
#     print(queue)
#
# while n!=1:
#     print("select the operation")
#     op=int(input("1)ENQUEUE, 2)DEQUEUE, 3)FRONT, 4)GEAR, 5)DISPLAY"))
#     if op==1:
#         enqueue()
#     elif op==2:
#         dequeue()
#     elif op==3:
#         front()
#     elif op==4:
#         gear()
#     elif op==5:
#         display()
#     n=int(input("press 1 to exit or press 0 to continue"))

#.......................................................................................................................
 ## QUEUE IMPLIMENTATION USING LINKED LIST ##

# from collections import deque
# queue=deque([])
# top=0
# size=int(input("enter the size of the queue"))
# n=1
# def enqueue():
#     global top,size
#     if top>size:
#         print("queue is overflowed")
#     else:
#         i=int(input("enter the element you want to add"))
#         queue.append(i)
#         top+=1
# def dequeue():
#     global top,size
#     if top<=0:
#         print("the queue is in underflow")
#     else:
#         queue.popleft()
#         top-=1
# def display():
#     print(queue)
# def front():
#     print("from element is ",queue[0])
# def rear():
#     print("last element is ",queue[-1])
# while n!=0:
#     print("choose the operation")
#     print("1.ENQUEUE, 2.DEQUEUE, 3.FRONT, 4.REAR, 5.DISPLAY")
#     c=int(input("enter the operation"))
#     if c==1:
#         push()
#     elif c==2:
#         pop()
#     elif c==3:
#         front()
#     elif c==4:
#         rear()
#     elif c==5:
#         display()
#     n=int(input("press 0 to exit or 1 to continue"))
#
#.......................................................................................................................

# singly linked list, append and iterate
# from collections import deque
# list=deque([])
# size=int(input("enter the size"))
# for j in range(0,size):
#     e=int(input("enter the elements you want to input"))
#     list.append(e)
# print(list)
# for i in list:
#
#     print(i)

#.......................................................................................................................

# TO CHECK A LIST EMPTY OF NOT #
# l=[]                   # if the list is not empty ,it wont print anything
# if not l:
#     print("list is empty")

#.......................................................................................................................

# EXAM QUESTION #
# print the employee detail with highest salary

# lst=[(1,"anu",28,20000),(2,"vinu",23,15000),(3,"ram",25,10000)]
# for i in range(0,len(lst)):
#     for j in range(0,len(lst)-i-1):
#         if lst[j][-1]>lst[j+1][-1]:
#             temp=lst[j]
#             lst[j]=lst[j+1]
#             lst[j+1]=temp
# print("the details of employee with highest salary is ",lst[-1])

#.......................................................................................................................
# to find whether the list is empty or not #

# l=[1,2,3,4]
# if len(l)==0:
#     print("empty")
# else:
#     print("not empty")

#..........................................................................................................

# to clone or copy list

# lst=[1,2,4,5,6]
# print("lst =",lst)
# b=list(lst)
# print("b =",b)

#..............................................................................................................

# write a python program to find the list of words that are longer than n from given list of words

# lst=["chikku","chinchu","minu","anu","aleena","akshara"]
# n=int(input("enter the length"))
# b=[]
# for i in lst:
#     if len(i)>n:
#         b.append(i)
# print(b)

#................................................................................................................
# write a python function that takes two lists and return True if they have at least one common member

# a=[1,2,3,"manu"]
# b=[4,3,5,"manu"]
# for i in a:
#     if i in b:
#         print("true")
#         break
#................................................................................................................

#print a specified list after removing 0th, 4th and 5th elements
# lst=[1,2,3,4,5,6,4,7]
# print(lst)
# b=[]
# c=[]
# b.append(lst[0])
# b.append(lst[4])
# b.append(lst[5])
# for i in lst:
#     if i not in b:
#         c.append(i)
# print(c)
#................................................................................................................

# write a python program to print  the numbers of a specified list after removing the even numbers from it
#
# lst=[1,2,3,4,5,6,7,8,9]
# b=[]
# for i in lst:
#     if i%2!=0:
#         b.append(i)
# print(b)

#................................................................................................................

# write a python program to shuffle and print a specified list

# from random import shuffle # use this code
# lst=[1,2,3,4,5,6,7,8,9]
# shuffle(lst)
# print(lst)

# from random import shuffle
# b=['green','yellow','red','blue','violet']
# shuffle(b)
# print(b)

#................................................................................................................
#write a python program to generate and print a list of first  and last 5 elements where the values are
# the square of numbers between 1 and 30.
# lst=[i**2 for i in range(1,31)]
# print("initial list :",lst)
# print(lst[:5])
# print(lst[-6:-1])

#.......................................................................................................................
# # to reverse a list
# lst = [10, 20, 30, 40, 50]
# print ("The reversed numbers are : ", end = "")
# lst.reverse()
# print(lst)

#.......................................................................................................................
# to reverse a list
# lst=[1,2,3,4,5,6]
# b=lst[::-1]
# print(b)

#.......................................................................................................................

# print done after execution of loop
# for i in range(0,5):
#     print(i)
# print("done!")

#.......................................................................................................................


#Given a number count the total number of digits in a number

# num=int(input("enter the number"))
# count=0
# while(num!=0):
#     num=num//10
#     count+=1
# print("count =",count)

#.......................................................................................................................

#Use a loop to display elements from a given list that are present at even index positions

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print("elements at the even indexes are ")
# for i in range(0,len(my_list)):
#     if(i%2==0):
#         print(my_list[i])
#.......................................................................................................................

# Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
# n=int(input("enter the number"))
# sum=0
# num=2
# for i in range(0,n): #i=0,      1           2            3
#     print(num,end=" ") #2       22          222          2222
#     sum+=num       #sum=0+2=2   2+=24       222+24=246   2222+246=2468
#     num=(num*10)+2 #num=20+2=22  220+2=222  2220+2=2222  22220+2=22222 (this wont be considered as n is only from 1=0 to 3)
# print()
# print(sum)  #2468

#.......................................................................................................................
# Write a Python program to import built-in array module and display the namespace of the said module.

# import array
# for name in array.__dict__:
#     print(name)

#.......................................................................................................................
#PYTHON
#django=?web application development

#front end#
#angular(fw)
#html
#css
#bootstrap
#javascript
#ajax
#jquery
#react(js library)

#back end use jango
# dataprocessing(python,java,c#,node,php,etc)
#data storing(databases)(mysql,postgres,sqlite) nosql(mongo db)

#Django FW(python)
#python
#class(design pattern,blueprint,template)
# real world entity- object(laptop,phone)
#database(mysql)
#.......................................................................................................................
#variable arguments in a function:
# def add(*args):
#     res=0
#     for n in args:
#         res+=n
#         print(res)
# add(10,20,30)
#.......................................................................................................................
# variable argument method with keyword and value
# def emp(**kwargs):
#     print(type(kwargs))
#     for k ,v in kwargs.items():
#         print(k,":",v)
# emp(name="Arjun",age=25,job="Engineer")
#..........................................................................................................
# arr=[10,8,11,9,12]
# #to sort in ascending order
# arr.sort() #here .sort is used to sort elements
# print(arr) # output= [8, 9, 10, 11, 12]
#
# # to sort in descending order
# arr.sort(reverse=True)
# print(arr) #[12, 11, 10, 9, 8]
#
# #arr.sort()= here sort() act as  a method inside a class
# #srt=sorted(arr) = here sorted is a function
#
# #ascending order
# srt=sorted(arr)
# print(srt)
#
# #descending order
# srt=sorted(arr,reverse=True)
# print(srt)
#.......................................................................................................
# employees={
#     1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
#     1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
#     1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
#     1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
#     1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
#
# }
#
#
# def print_employee(**kwargs): #dict format= {id:1000,prop:"salary}
#     id=kwargs['id'] # we use double quotes to call the keyword
#     prop=kwargs['prop']
#     if id in employees:
#         print(employees[id]['name'])
#         print(employees[id][prop])
#
# print_employee(id=1000,prop='salary') # name, salary
# print()
# print_employee(id=1002,prop='designation')

#.......................................................................................................................

