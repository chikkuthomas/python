# EXCEPTIONAL ERROR HANDLING #
#1) arithmetic error

# a=int(input("enter the number"))
# b=int(input("enter the number 2"))
# try:
#     print(a/b)       #here the exceptional error occurrs at the operation
# except:
#     print("exception error occurred")
# finally:
#     print("you are done")

#try,except and finally blocks can act together

#.......................................................................................................................

# TYPE ERROR #

#where instead of integer we enter string for arithmetic operation
# try:
#     a=int(input())
#     b=int(input())
#     print(a+b)
# except:
#     print("please enter an integer value")
# finally:
#     print("you are done")

#.......................................................................................................................

# INDEX ERROR #

# lst=[1,2,3,4,5,6,78,9]
# i=int(input("enter the index value"))
# try:
#     print(lst[i])
# except:
#     print("list out of range")
# finally:
#     print("done")

#.......................................................................................................................

# CLASS #
# class Score:
#     def cricket(self):
#         print("the score is high")
#     def football(self):
#         print("the score is low")
#
# p=Score()
# p.cricket()
# p.football()

#..................................................................................................................................
# CLASS WITH ATTRIBUTES  #
# class Person:
#     def details(self,name,age,salary,job):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.job=job
#     def print(self):
#         print(self.name)
#         print(self.age)
#         print(self.salary)
#         print(self.job)
# o=Person()
# o.details("chikku",26,1000000,"engineer")
# o.print()

#.......................................................................................................................

# to add two numbers #
# class Addition:
#     def add(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#         print("sum =",self.num1+self.num2)
# o=Addition()
# o.add(8,12)
#
# p=Addition()
# p.add(99,1)
#.......................................................................................................................

# create a class to print employee details

#employee class

# class Employee:
#     company="Tesla"
#     def details(self,name,id,age,salary,department):
#         self.name=name
#         self.id=id
#         self.age=age
#         self.salary=salary
#         self.department=department
#         print("name =",self.name)
#         print("age =",self.age)
#         print("id =",self.id)
#         print("salary =",self.salary)
#         print("department =",self.department)
#         print("company =",Employee.company)
# o=Employee()
# o.details("Chikku",45783,26,80000,"engineering")

#.......................................................................................................................

# CREATE A STUDENT LIST THE SAME SCHOOL #

#.......................................................................................................................

## BANK ACCOUNT ##

# 1) ACCOUNT CREATION,2)MINIMUM BALANCE,3)DEPOSIT MONEY 4)WITHDRAWAL MONEY 5)INSUFFICIENT BALANCE
# class Bank:
#     bank="SBI"
#     def account(self,name,age):
#         self.name=name
#         self.age=age
#         self.minbalance=5000
#         print("name =",self.name)
#         print("age =", self.age)
#         print("minbalance =", self.minbalance)
#         print("bank =",Bank.bank)
#     def deposit(self,damt):
#         self.damt=damt
#         self.minbalance+=self.damt
#         print("current balance is ",self.minbalance)
#     def withdraw(self,wamt):
#         self.wamt=wamt
#         if self.wamt>self.minbalance:
#             print("insufficient balance")
#         else:
#             self.minbalance-=self.wamt
#             print("current balance is ",self.minbalance)
#
# o=Bank()
# o.account("chikku",27)
# o.deposit(600000)
# o.withdraw(18000000)

#.......................................................................................................................
 # CONSTRUCTOR #

# class Person:
#      def __init__(self,name,age,gender):
#          self.name=name
#          self.age=age
#          self.gender=gender
#      def printval(self):
#          print("name :",self.name)
#          print("age :",self.age)
#          print("gender :",self.gender)
# o=Person("Chikku",26,"Female")
# o.printval()
#.......................................................................................................................

# STUDENT CLASS USING CONSTRUCTOR #

# class Student:
#     school="St.treasa's"
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
#     def print(self):
#         print("name :",self.name)
#         print("age :", self.age)
#         print("id :", self.id)
#         print(Student.school)
#         print()
# b=Student("Chikku",10,4785)
# b.print()
#
# n=Student("Chinchu",10,7857)
# n.print()
#
# m=Student("Minu",14,4583)
# m.print()
#.......................................................................................................................

# CALCULATOR USING CONSTRUCTOR #
#
# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def add(self):
#         print("sum =",self.num1+self.num2)
#
#     def sub(self):
#         print("sub =", self.num1 - self.num2)
#
#     def mul(self):
#         print("mul =", self.num1 * self.num2)

#     def div(self):
#         print("div =", self.num1 / self.num2)
#
# b=Calculator(8,2)
# b.add()
# b.sub()
# b.mul()
# b.div()

#.......................................................................................................................

# SINGLE INHERITANCE #
# class Person:    #super class, parent class, base class
#     def details(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         print(self.name)
#         print(self.age)
#         print(self.gender)
#
# class Employee(Person):  # sub class, child class, derived class
#     company="TESLA"
#     def det(self,salary,department):
#         self.salary=salary
#         self.department=department
#         print(self.salary)
#         print(self.department)
#         print()
#
# class Student(Person):
#     school="xyz"
#     def school(self,division):
#         self.division=division
#         print("division =",self.division)
#
# o=Employee()
# o.details("chikku",26,"female")
# o.det(50000000,"ENGINEERING")
#
# p=Student()
# p.details("Chinchu",12,"female")
# p.school(7)

#.......................................................................................................................
#multiple inheritance

# class Person:
#     def details(self):
#         print("chikku")
# class Parent:
#     def par(self):
#         print("lovely and")
# class Child(Person,Parent):
#     def det(self):
#         print("is smart")
# p=Child()
# p.details()
# p.det()
# p.par()
#.......................................................................................................................

#multi level inheritance

# class Person:
#     def details(self):
#         print("chikku")
# class Parent(Person):
#     def par(self):
#         print("lovely and")
# class Child(Parent):
#     def det(self):
#         print("is smart")
# c=Child()
# c.details()
# c.par()
# c.det()
# print()
#
# p=Parent()
# p.details()
# p.par()

#.......................................................................................................................

#create a vehicle class with max speed and mileage instance attributes

# class Vehicle:
#     def veh(self,max_speed,mileage):
#         self.max_speed=max_speed
#         self.milleage=mileage
#         print("max_speed :",self.max_speed)
#         print("mileage :",self.milleage)
# o=Vehicle()
# o.veh(70,65)

#.......................................................................................................................

# # create a vehicle class without any variables or methods
# class Vehicle:
#     pass

#.......................................................................................................................

#create a childclass bus that will inherit all of the methods of vehicle class
#
# class Vehicle:
#     def bus(self,name,max_speed,mileage):
#         self.name=name
#         self.max_speed=max_speed
#         self.mileage=mileage
#         print("name: ",self.name)
#         print("max speed: ",self.max_speed)
#         print("mileage: ",self.mileage)
# class Bus(Vehicle):
#     pass
# o=Bus()
# o.bus("School volvo ",180,12)

#.......................................................................................................................

#Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity()
# a default value of 50.
#
# class Vehicle:
#     def __init__(self,name,max_speed,mileage):
#         self.name=name
#         self.max_speed=max_speed
#         self.mileage=mileage
#     def capacity(self,capacity):
#         self.capacity=capacity
#         print("the seating capacity of a",self.name,"is",self.capacity)
#
# class Bus(Vehicle):
#     pass
#
#
# o=Vehicle("volvo bus",0,0)
# o.capacity(50)

#.......................................................................................................................

#Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

#Use the following code for this exercise.
# class Vehicle:
#     colour='white'
#     def __init__(self,name,max_speed,mileage):
#         self.max_speed=max_speed
#         self.name=name
#         self.mileage=mileage
#
# class Car(Vehicle):
#     pass
# class Bus(Vehicle):
#     pass
# bus=Bus("volvo",85,5)
# print("colour: ",Vehicle.colour,"vehicle name:",bus.name,"vehicle mileage: ",bus.mileage,"vehicle speed: ",bus.max_speed)
# print()
# car=Car("Audi R8",87,3)
# print("colour: ",Vehicle.colour,"vehicle name:",bus.name,"vehicle mileage: ",bus.mileage,"vehicle speed: ",bus.max_speed)
# # we can call all instance variable by the object (reference) only // not with self //
#............................................................................................................................

#Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

# here take the seat capacity as 50

# class Vehicle:
#     def __init__(self,name,speed,mileage,capacity):
#         self.name=name
#         self.speed=speed
#         self.mileage=mileage
#         self.capacity=capacity
# class Bus(Vehicle):
#     def fare(self):
#         self.amount=self.capacity*100
#         self.amount+=self.amount*(10/100)
# bus=Bus("volvo",85,3,50)
# bus.fare()
# print("total bus fare =",bus.amount)

#.......................................................................................................................

# Determine which class a given Bus object belongs to (Check type of an object)
#
# class Vehicle:
#     def __init__(self,name,mileage,capacity):
#         self.name=name
#         self.mileage=mileage
#         self.capacity=capacity
#         print("name: ",self.name)
#         print("mileage: ",self.mileage)
#         print("capacity: ",self.capacity)
# class Bus(Vehicle):
#     def type(self):
#         pass
#
# bus=Bus("volvo",5,50)
# bus.type()
# print(type(bus))  # to find the type of object

#.......................................................................................................................

# Determine if School_bus is also an instance of the Vehicle class
# class Vehicle:
#     def __init__(self,name,mileage,speed):
#         self.name=name
#         self.mileage=mileage
#         self.speed=speed
# class Bus(Vehicle):
#     pass
# bus=Bus("volvo",5,85)
# print(isinstance(bus,Vehicle))   # comparing with the object, checking whether the object is an instance of superclass
                                 # Vehicle  "isinstance" built in keyword

#...................................................................................................................

#constructor and inheritence
#
# class Person:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def print(self):
#         print(self.name)
#         print(self.age)
#         print(self.gender)
# class Employee(Person):
#     company="TCS"
#     def __init__(self,id,salary,department,name,age,gender):
#         super().__init__(name,age,gender)
#         self.id=id
#         self.salary=salary
#         self.department=department
#     def det(self):
#         print(self.id)
#         print(self.salary)
#         print(self.department)
#         print("company: ",Employee.company)
#     def __str__(self):
#         return self.name + str(self.id)
#
# o=Employee(5,500000,"EEE","anju",25,"female")
# o.print()
# o.det()
# print()
# print(o)
#.....................................................................................................................

#constructor inheritance
# class Book:
#     def __init__(self,name,author):
#         self.name=name
#         self.author=author
#     def print(self):
#         print("book name: ",self.name)
#         print("author name: ",self.author)
# class Det(Book):
#     def __init__(self,year,price,name,author):
#         super().__init__(name,author)
#         self.year=year
#         self.price=price
#     def val(self):
#         print("year of publishing: ",self.year)
#         print("price of the book: ",self.price,"rs")
#     def __str__(self):
#         return self.name+self.author
# bk=Det(1994,400,"The Stars And The Moon","A J John")
# bk.print()
# bk.val()
# print()
# print(bk)
# print(type(bk))
# print(isinstance(bk,Book))


#.....................................................................................................................

#over-riding
# class Person:
#     def smile(self):
#         print("take my smile")
# class Student(Person):
#     def smile(self):
#         print("give me your smile")
# o=Student()
# o.smile()


#.............................................................................................................

# to read values from text file and print if the mark value is >190
# details
# anu,1,bca,200
# rahul,2,bba,177
# vinod,3,bba,187
# manju,4,engg,250
# anagha,5,mca,260
#
# class Students:
#     def print(self,name,rollno,dep,mark):
#         self.name=name
#         self.rollno=rollno
#         self.dep=dep
#         self.mark=mark
#         print("name: ",self.name)
#         print("rollno: ",self.rollno)
#         print("department: ",self.dep)
#         print("mark: ",self.mark)
# f=open("file1","r")
# for line in f:
#     data=line.rstrip("\n").split(",")
#     name=data[0]
#     rollno=data[1]
#     dep=data[2]
#     mark=data[3]
#     o=Students()
#     if int(mark)>190:
#         o.print(name,rollno,dep,mark)
#         print()


#...............................................................................................................

# if u want to print only name of the students
# class Student:
#     def print(self,name,rollno,dep,mark):
#         self.name=name
#         self.rollno=rollno
#         self.dep=dep
#         self.mark=mark
#         print(self.name)
#         print(self.rollno)
#         print(self.dep)
#         print(self.mark)
# lst=[]
# f=open("file1","r")
# print("students with mark greater than 190")
# for line in f:
#     det=line.rstrip("\n").split(",")
#
#     if int(det[3])>190:
#         name=det[0]
#         lst.append(det)
#         p=Student()
#         print(name)

#.......................................................................................................................

# REGULAR EXPRESSION
# to check pattern matching and whether  the input is validated
# to validate email id, username,phone number

# TO print matches, positions and matching string at each position
# to print the count of matches in both strings
# import re
# count=0
# match=re.finditer('ab','abababaabbbab')
# for i in match:
#     print("the matching positions: ")
#     print(i.start())
#     print("the string compared: ",i.group())
#     count+=1
# print("count= ",count)

#.......................................................................................................................

# to count the number of matches
# import re
# count=0
# a=re.finditer('ch','chikkuchinchu minu')
# for i in a:
#     count+=1
# print("count of matches: ",count)

#.......................................................................................................................

#RULE

# rule 1 - matching with either of the alphabets given

# x='[abc]' # either a b or c is checked for matching
# import re
# f=re.finditer(x,"chikku thomas")
# for i in f:
#     print("available positions: ",i.start())
#     print("matches: ",i.group())
#     print()

#.......................................................................................................................

# 2) Not matching with the given alphabets

# x='[^abc]'
#
# import re
# f=re.finditer(x,"chikku thomas")
# for i in f:
#     print("available positions: ",i.start())
#     print("matches: ",i.group())
#     print()
#.......................................................................................................................

# x='[a-z]'
#
# import re
# f=re.finditer(x,"chikku thomas")
# for i in f:
#     print("available positions: ",i.start())
#     print("matches: ",i.group())
#     print()

# x='[A-Z]'

# f=re.finditer(x,"chikku thomMas")
# for i in f:
#     print("available positions: ",i.start())
#     print("matches: ",i.group())
#     print()

# x='[a-zA-Z]'
#
# f=re.finditer(x,"chikku thomMas")
# for i in f:
#     print("available positions: ",i.start())
#     print("matches: ",i.group())
#     print()
#
# x='[^a-zA-Z0-9]'

# f=re.finditer(x,"chikku t&#homMas")
# for i in f:
#     print("available positions: ",i.start())
#     print("matches: ",i.group())
#     print()

# x='[\s]'
# f=re.finditer(x,"chikku t&#homMas")
# for i in f:
#     print("available positions: ",i.start())
#     print("matches: ",i.group())
#     print()

# x='[\d]'
# f=re.finditer(x,"ch7ik5ku t&#homMas")
# for i in f:
#     print("available positions: ",i.start())
#     print("matches: ",i.group())
#     print

# x='[\D]'
# f=re.finditer(x,"ch7ik5ku t&#homMas")
# for i in f:
#     print("available positions: ",i.start())
#     print("matches: ",i.group())
#     print()

# x='[\w]'
# # f=re.finditer(x,"ch7ik5ku t&#homMas")
# # for i in f:
# #     print("available positions: ",i.start())
# #     print("matches: ",i.group())
# #     print()

# x='[\W]'
# f=re.finditer(x,"ch7ik5ku t&#homMas")
# for i in f:
#     print("available positions: ",i.start())
#     print("matches: ",i.group())
#     print()

#................................................................................................................

# QUANIFIERS
# 1) x='a' - if a is included in the the grp

import re
# x='a'
# r='abc aaa agc gfa'
# match=re.finditer(x,r)
# for i in match:
#     print("match available at: ",i.start())
#     print("groups: ",i.group())


#................................................................................................................

# x='a*' #- #a included in the grp and the zero number of a
# r='abc aaa agc gfa'
# match=re.finditer(x,r)
# for i in match:
#     print(i.start())
#     print(i.group())
#     print()

#.................................................................................................................

# x='a?' # counted a and zero places of a as each element instead of string
# r='aab aaaa cag'
# match=re.finditer(x,r)
# for i in match:
#     print(i.start())
#     print(i.group())
#     print()

#................................................................................................................

# x='^a' #if the string is starting with a
# r='aaa abc agc dhl'
# match=re.finditer(x,r)
# for i in match:
#     print(" starting with a")

#................................................................................................................

# x='a$' # ending with a
# r="aaa abc ahf aga"
# m=re.finditer(x,r)
# for i in m:
#     print("ending with a")

#.......................................................................................................................

# to validate "hello"
# r='hello'
# x='\w'
# m=re.finditer(x,r)
# if m is not None:
#         print("valid")


#.......................................................................................................................

# #to validate 56kg
# r="56kg"
# x='\d\w'
# m=re.finditer(r,x)
# if m is not None:
#     print("valid")
# else:
#     print("not valid")

#.......................................................................................................................

# to validate phone number
# r=input("enter the phone number")
# x='[+][9][1]\d{10}'
# m=re.fullmatch(x,r)
# if m is not None:
#     print("valid")
# else:
#     print("not valid")

#..........................................................................................................................

#to validate email
import re
# r=input("enter the email")
# x='[a-z0-9]+[@]+\w+[.][c][o][m]'
# m=re.fullmatch(x,r)
# if m is not None:
#     print("valid email")
# else:
#     print("not a valid email")

# '[a-z0-9]+[@]+\w+[.][c][o][m]'
# [a-z0-9] = here only small alphabets are numbers are allowed in the first place (chikkuthomas10)
#[@]= next portion @ if the format
# \w = here gmail,yahoo etc is a word format
#[.][c][o][m]= the last format of an email is .com
# here "+" is added according to the format and position of the rule

#.................................................................................................................

# Write a Python program to check that a string contains only
# a certain set of characters (in this case a-z, A-Z and 0-9)

# import re
# r='hi my age is A 98'
# x='[a-zA-Z0-9]'
# f=re.finditer(x,r)
# if f is not None:
#     print("matching")

#.................................................................................................................

#Write a Python program that matches a string that has an a followed by zero or more b's
# import re
# r=input("enter the string")
# x='^ab?' #* means including zero, ? one or more occurrance
# f=re.search(x,r)
# if f is not None:
#     print("matching")

#...............................................................................................................

# Write a Python program to check that a string contains only
# a certain set of characters (in this case a-z, A-Z and 0-9)
# import re
# r=input("enter the string")
# x='[a-zA-Z0-9]+'
# f=re.fullmatch(x,r)
# if f is not None:
#     print("matching")
# else:
#     print("not matching")

#....................................................................................................................

#starting with 'a' and ending with 'b', in btwn anything can come
# r=input("enter the string")
# x='^a[a-zA-Z0-9\W]+b$'
# f=re.fullmatch(x,r)
# if f is not None:
#     print("valid")
# else:
#     print("invalid")

#..............................................................................................................

#string with minimum length 8 and max length 15,numbers not allowed
# r=input("enter the string")
# x='[a-zA-Z]{8,15}'
# f=re.fullmatch(x,r)
# if f is not None:
#     print("valid")
# else:
#     print("invalid")

#....................................................................................................................

# validate a mail id
# r=input("enter the email id")
# x='^[a-z0-9]+@\w+[.][c][o][m]$'
# f=re.fullmatch(x,r)
# if f is not None:
#     print("valid")
# else:
#     print("invalid")

#.....................................................................................................................

# # kerala vehicle number validation
# r=input("enter the string")
# x='^[K][L][0-9]{2}[A-Z]{2}\d{4}'
# f=re.fullmatch(x,r)
# if f is not None:
#     print("valid")
# else:
#     print("invalid")

#....................................................................................................................

# class Student:
#     pass
# class Marks:
#     pass
# student=Student()
# marks=Marks()
# print(isinstance(student,Student))
# print(isinstance(marks,Marks))
# print(isinstance(student,Marks))
# print(isinstance(Marks,Student))
# print(issubclass(Student,object))
# print(issubclass(Marks,object))

#.......................................................................................................................

#The most occurring number in a string using Regex in python
#eg: chhhhh44jjjhuyh44kkjutg

#................................................................................................................

# import re
# r=input()
# x='^[L][U][M][0-9]{2}[P][Y][0-9]{3}'
# f=re.fullmatch(x,r)
# if f is not None:
#     print("match")
# else:
#     print("invalid")
# multiple inheritance

#..............................................................................................................

# \s will match any white space character "," , "."

#...............................................................................................................

# Create a child class Bus that will inherit all of the variables and methods of Vehicle class?
# class Vehicle:
#     def details(self,type,maxspeed):
#         self.type=type
#         self.maxspeed=maxspeed
#
#         print("Vehicle type: ",self.type)
#         print("max speed: ",self.maxspeed,"km/hr")
# class Bus(Vehicle):
#     pass
# v=Bus()
# v.details("bus",78)
# print()
# k=Bus()
# k.details("car",85)

#..............................................................................................................

# Create a Book class with instance Library_name, book_name, author, pages?
# class Book:
#     Library_name="abc"
#
#     def details(self,book_name,author,pages):
#         self.name=book_name
#         self.author=author
#         self.page=pages
#         print("library name: ",Book.library_name)
#         print("Book name: ",self.name)
#         print("Author: ",self.author)
#         print("No of pages: ",self.page)
# book=Book()
# book.details("A454","WHY WE TOOK THE CAR","A K MAX",345)
# print()

#..................................................................................................................

#Create an Animal class using constructor and build a child class for Dog?
# class Animal:
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type
#
#     def print(self):
#         print("Animal name: ",self.name)
#         print("Animal type: ",self.type)
#
# class Dog(Animal):
#     def __init__(self,petname,name,type):
#         super().__init__(name,type)
#         self.petname=petname
#
#     def printval(self):
#         print("Pet name: ",self.petname)
#
#
# b=Dog("Pinky","dog","domestic")
# b.print()
# b.printval()

#............................................................................................................

#What is method overriding give an example using Books class?
# class Book:
#     def details(self,name,pages):
#         self.name=name
#         self.pages=pages
#         print("name: ", self.name)
#         print("Pages: ", self.pages)
#         print("bad")
# class Page(Book):
#     def details(self,name,pages):
#         self.name=name
#         self.pages=pages
#         print("name: ",self.name)
#         print("Pages: ",self.pages)
#         print("good")
# book=Page()
# book.details("Why we took the car",354)

#..........................................................................................................

## method overriding is where the parent class and child class has same method names and
# the number of parameters are also same, such that the
# child class method will over ride the parent class method when the program is executed.

#When is the finally block executed.Explain with example?

# a=10
# b=0
# try:
#     print("ans: ",a/b)
# except:
#     print("exceptional error occurred")
# finally:
#     print("done")

#Write a Python program to find the sequences of one upper case letter followed by lower case letters?
# import re
# r=input("enter the string")
# x='^[A-Z]{1}[a-z]+'
# match=re.fullmatch(x,r)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

#.............................................................................................................

#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
# import re
# r=input("enter the string")
# x='^a[a-zA-Z0-9\D]+b$'
# match=re.fullmatch(x,r)
# if match is not None:
#     print("matching")
# else:
#     print("not matching")

#..............................................................................................................

#Create an example for three types of inheritance in one program by using Person as main class?
# class Person:
#     def print(self,name):
#         self.name=name
#         print(self.name)
#
#
# class Student:
#     def printval(self,age):
#         self.age=age
#         print(self.age)
#
# # single inheritance #
# class Print(Person):
#     def m(self):
#         print("details:")
#
# # multiple inheritance #
# class Parent(Person,Student):
#     def det(self,job):
#         self.job=job
#         print(self.job)
#
# # multi level inheritance #
# class Employee(Parent):
#     def details(self,salary):
#         self.salary=salary
#         print(self.salary,"Rs")
#
#     def __str__(self):
#         return self.name
#
# v=Print()
# v.m()
#
# o=Employee()
# o.print("Maneesh")
# o.printval(25)
# o.det("Engineer")
# o.details(50000)
# print()
# print(o)

#..................................................................................................................

## Create a valid phone numbers file from the following file?
# +915678905432 +914567890321 765432167 123450987765 +919976532456

# import re
# lst=[]
# f=open("phone","r")
# for i in f: # to iterate each the file content
#     d=i.rstrip("\n") #to stripout th "\n"
#     lst.append(d)  # after stripping to add elements to the list
#
# for j in lst: # to iterate each element in list and check
#     x='^[+][9][1]\d{10}'
#     ph=re.fullmatch(x,j) # matching each element with x
#     if ph is not None:   #if matching
#         w=open("num.txt","a") #here append is used since we need to add all
#
#         w.write(j)
#         w.write("\n") # to print in next line

#..............................................................................................................

# #Create objects of the following file and print the details of student
# # with maximum mark? anu,1,bca,200 rahul,2,bba,177 vinod,3,bba,187 ajay,4,bca,198 maya,5, bba,195
# #
# class Student:
#     def details(self,name,rollno,department,mark):
#         self.name=name
#         self.roll=rollno
#         self.dep=department
#         self.mark=mark
#         print("NAME: ",self.name)
#         print("ROLL NO: ",self.roll)
#         print("DEPARTMENT: ",self.dep)
#         print("MARK: ",self.mark)
# f=open("mark","r")
# lst=[]
#
# for line in f:
#     data=line.rstrip("\n").split(",")
#     lst.append(data)#[[anu,1,bca,200],[rahul,2,bba,177],[vinod,3,bba,187],[ajay,4,bca,198],[maya,5, bba,195]
# print(lst)
# for i in range(0,len(lst)):#(0,5) i=0       1       2     3
#     for j in range(0,len(lst)-i-1):#j=(0,4)  (0,3)  (0,2)  (0,1)
#         if lst[j][-1]>lst[j+1][-1]:
#
# # lst[0][-1]>lst[1][-1]
# # " [anu,1,bca,200]"=200 > 100 "[rahul,2,bba,177]" {TRUE}
#             temp=lst[j]     #temp=[anu,1,bca,200]
#             lst[j]=lst[j+1] #lst[0]=[rahul,2,bba,177]
#             lst[j+1]=temp   #lst[1]=[anu,1,bca,200]
# # new lst=[[rahul,2,bba,177],[anu,1,bca,200],[vinod,3,bba,187],[ajay,4,bca,198],[maya,5, bba,195]]
#
# #i=1, j=(0,3)
# #lst[1][-1]>lst[2][-1]
# #"[anu,1,bca,200]"= 200 > 187 "[vinod,3,bba,187]" {true}
# # temp=[anu,1,bca,200]
# # lst[1]=[vinod,3,bba,187]
# # lst[2]=[anu,1,bca,200]
#
# #new lst=[[rahul,2,bba,177],[vinod,3,bba,187],[anu,1,bca,200],[ajay,4,bca,198],[maya,5, bba,195]]
#
# # so here finally the details of the student with maximum mark will take the last element position in list
# #i.e lst[-1]
#
# name=lst[-1][0]
# roll=lst[-1][1]
# dep=lst[-1][2]
# mark=lst[-1][3]
#
# print("details of student with maximum mark")
# o=Student()
# o.details(name,roll,dep,mark)

#................................................................................................................

# class Student:
#     def __init__(self,name,rollno,course,mark):
#         self.name=name
#         self.roll=rollno
#         self.dep=course
#         self.mark=mark
#     def print(self):
#         print(self.name)
#         print(self.dep)
#         print(self.roll)
#         print(self.mark)
# lst=[]
# f=open("mark","r")
# for i in f:
#     d=i.rstrip("\n").split(",")
#     name=d[0]
#     roll=d[1]
#     dep=d[2]
#     mark=d[3]
#     s1=Student(name,roll,dep,mark)
#     lst.append(s1)
# mark=[]
# for st in lst:
#     mark.append(st.mark)
# for st in lst:
#     if (st.mark==max(mark)):
#         print(st.name,st.roll,st.dep,st.mark)

#.......................................................................................................................

# DUCT TYPING

# class Swift:
#     def start(self):
#         print("start swift car")
#     def accelerate(self):
#         print("swift car accelerating")
#     def stop(self):
#         print("swift car is stopping")
# class Audi:
#     def start(self):
#         print("audi is starting")
#     def accelerate(self):
#         print("audi car is accelerating")
#     def stop(self):
#         print("audi car is stopping")
# class Person:
#     def drive(self,car):
#         car.start()
#         car.accelerate()
#         car.stop()
# p=Person()
# sw=Swift()
# p.drive(sw)
# print()
# ad=Audi()
# p.drive(ad)

#......................................................................................................................

# class Pycharm:
#     def compile(self):
#         print("compile in pycharm")
#     def execute(self):
#         print("execute in pycharm")
# class Vscode:
#     def compile(self):
#         print("compile in vscode")
#     def execute(self):
#         print("execute in vscode")
# class Person:
#     def print_val(self,ide):
#         ide.compile()
#         ide.execute()
# p=Person()
# py=Pycharm()
# p.print_val(py)

#........................................................................................................................

# # LAMBDA
# sum=lambda num1,num2:num1+num2
# print(sum(10,2))
#
# sub=lambda num1,num2:num1-num2
# print(sub(10,2))
#
# div=lambda num1,num2:num1/num2
# print(div(10,2))
#
# mul=lambda num1,num2:num1*num2
# print(mul(10,2))

#......................................................................................................................

# map() is used when we want to get all elements in the list to be worked upon
#eg: from a list increment all the numbers by 1
#eg1: from a list make all the names into uppercase

# SYNTAX = map(fun, iter)

# The map() function applies a given to function to each item of an iterable and returns a list of the results.
# The returned value from map() (map object) can then be passed to functions like list()
# (to create a list), set() (to create a set) and so on.

# lst=[1,2,3,4]
# # normal function for incrementing
# def incre(num):
#     return num+1

#
# #using map function and function method
# inc=list(map(incre,lst))
# print(inc)
#
# # using map and lambda
# inp=list(map(lambda num:num+1,lst))
# print("incremented list:",inp)

#.......................................................................................................................

# UPPER CASE NAMES #
# lst=['ajay','arun','nikhil','nivin']
# uppername=list(map(lambda name:name.upper(),lst))
# print("upper cae names list:",uppername)

#.......................................................................................................................

# INCREMENT AND DECREMENT WITHIN A LIST #
# lst1=[7,8,9,4,3,1]
# l=list(map(lambda num:num+1 if num>5 else num-1,lst1))
# print(l)

#.......................................................................................................................

# SQUARE OF THE NUMBERS IN A LIST #
# lst=[1,2,3,4,5,6]
# l=list(map(lambda num:num**2,lst))
# print(l)

#.......................................................................................................................

# how to use map function
# l=map(lambda num:fn, iteratbale)
# here iterable is on which the map function has to be carried out

#.......................................................................................................................
#.......................................................................................................................

# # filter()= FILTER FUNCTION
# # filter function is used when we need the elements which satisfy the given condition

# lst=[1,2,3,4,5,6]
# # to print numbers greater than 5
# l=list(filter(lambda num:num>2,lst))
# print(l)

# # num
# #the condition
# #iterable
#.......................................................................................................................

# # PRINT NAMES STARTING WITH C

# lst=['anju','chinchu','chikku','maneesh','chandran']
# l=list(filter(lambda name:name[0]=='c',lst))
# print(l)

#.......................................................................................................................

#print odd numers

# lst=[1,2,3,4,5,6,7,8,9]
# l=list(filter(lambda num:num%2!=0,lst))
# print("odd number list",l)
#.......................................................................................................................
# # List of strings
# l = ['sat', 'bat', 'cat', 'mat']
# test=list(map(list,l))
# print(test)

#.......................................................................................................................
# calculate the length of each word in a tuple
# tup=('apple', 'banana', 'cherry')
# t=list(map(lambda i:len(i),tup))
# print(t)

#.......................................................................................................................

#Write a Python program to triple all numbers of a given list of integers. Use Python map.
# lst=[1,2,3,4,5,6]
# l=list(map(lambda num:num*3,lst))
# print(l)

#.......................................................................................................................

 #Write a Python program to add three given lists using Python map and lambda
# l1=[1,2,3,4,5,6]
# l2=[10,20,30,40,50,60]
# l3=[100,200,300,400,500,600]
# lst=list(map(lambda x,y,z:x+y+z,l1,l2,l3)) # here inorder to iterate three lists we can use three arguments
# print(lst)
#.......................................................................................................................
# Write a Python program to create a list containing the power of said number
# in bases raised to the corresponding number in the index using Python map

# base=[10,12,30,14,50]
# index=[1,2,3,4,5]
# l=list(map(pow,base,index))
# print(l)
#pow() is given to map two list objects, one for each base and index parameter
#.......................................................................................................................

# write a program to convert each characters in upper case an lower case and then eliminate duplicate characters
# def chara(l):
#     for i in l:
#         return str(l).upper(),str(l).lower()
# # here we use str(l).upper() otherwise it will become error
# l=['u','F','g','H','k','a','L','L']
#
# new=set(map(chara,l)) # we use set() to eliminate duplicate elemets
# print(new)

#.......................................................................................................................

# employees = [
#     {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
#     {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
#     {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
#     {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
#     {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
#
# ]
# # to print the names of employees using map and list comprehension
# enames=list(map(lambda emp:emp['name'],employees))
# print("names using map():",enames)
#
# e_names=[emp['name'] for emp in employees]
# print("names using list comprehension:",e_names)


# upnames=list(map(lambda emp:emp['name'].upper(),employees))
# print("using map:",upnames)
# unames=[emp['name'].upper() for emp in employees]
# print("uppercase names using list comprehension:",unames)

# print employe deatails whose name starting with 'a'   ==a  filter()
# a_names=list(filter(lambda emp:emp['name'][0]=='a',employees))
# print("filter() names:",a_names)
# anames=[emp['name'] for emp in employees if emp['name'][0]=='a']
# print("using lst comp:",aname

# #print employee details whode salary > 23000  filter()
# esal=list(filter(lambda emp:emp['salary']>23000,employees))
# print("using filter():",esal)
# e_sal=[emp for emp in employees if emp['salary']>23000]
# print("using lst comp:",e_sal)

# # print employee details whose designation==developer
# e_des=list(filter(lambda emp:emp['designation']=='developer',employees))
# print('using filter:',e_des)
# edesi=[emp for emp in employees if emp['designation']=='developer']
# print(edesi)

# #in developers whose salary abv 24000
# edsal=list(filter(lambda emp:emp['designation']=='developer' and emp['salary']>24000,employees))
# print(edsal)
# e_dsal=[emp for emp in employees if emp['designation']=='developer' and emp['salary']>24000]
# print("using lst comp:",e_dsal)

#highest salary
# from functools import *
# highest=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
#                list(map(lambda emp:emp['salary'],employees)))
# print("using reduce:",highest)

#.......................................................................................................................

#highest salary
# fruits=['mango','apple','orange']
# frt=[(fruit,fruit)for fruit in fruits]
# print(frt)

# lst1=[1,2]
# lst2=[10,20]
# lst=[(num1,num2) for num1 in lst1 for num2 in lst2]
# print(lst)

# lst3=[7,8,9,4,2]
# # 8,9,10,3,1
# lst=[num+1 if num>5 else num-1 for num in lst3]
# print(lst)

#to find the total using  reduce method
# arr=[1,2,3,4,5,6,7,8,9,10]
# from functools import *
# total=reduce(lambda num1,num2:num1+num2,arr)
# print(total)
#
# #in reduce we can use two parameters
# #only numbers are allowed
# #need to import reduce function from functiontools bcs it is not imported
#
# #highest in the grp
# high=reduce(lambda num1,num2:num1 if num1>num2 else num2,arr)
# print(high)

#.......................................................................................................................

# [:n] is used when u want to print the elements of given list till some length of the list

#Returns the n maximum elements from the provided list.
# If n is greater than or equal to the provided list's length,
# then return the original list (sorted in descending order)
#
# def n_elements(lst,n):
#     return sorted(lst,reverse=True)[:n] # t get the sorted list in decending order
#                                         # and to get the n number of elements nlu
# print("list:",n_elements([4,1,5,2,3,7],3))# here only 3 elements of sorted list will be shown in op
# print("list1:",n_elements([4,8,6,3,2,9],15)) # here the value f n is greater than the length of the list
                         # hence all the elements in the descending order list will be shown in the op as in the list

#.......................................................................................................................

#1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result.
#
# numb=lambda num:num+15
# print(numb(10))
#
# mul=lambda x,y:x*y
# print(mul(3,5))

#.......................................................................................................................

#Write a Python program to create a function that takes one argument,
# # and that argument will be multiplied with an unknown given number.
# def mul(n):
#     return lambda x:x*n
# result=mul(2)
# print(result(15))

#.......................................................................................................................

#3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# SORTING LIST OF TUPLES USING THE SECOND VALUE OF EACH TUPLE

# here we use key in sorting,because here we want to do the sorting based on the second value in the tuple ,
# This key function transforms each element before sorting, it takes the value and returns 1 value which is then used
# within sort instead of the original value. Key also takes user-defined functions as its value for the basis of sorting.

# l=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# l.sort(key=lambda x:x[1]) # here instead of the whole tuple the 1st index values are taken to consider for sorting
# print(l)

#.......................................................................................................................

# # 5.Python code to print the details of employee with maximum salary using lambda and sort/sorting

# lst=[(1,"anu",28,20000),(2,"vinu",23,15000),(3,"ram",25,10000)]

#using sort
# lst.sort(key=lambda x:x[3])
# print(lst[2])

#using sorting
# l=sorted(lst,key=lambda x:x[3])
# print(l[2])

#.......................................................................................................................

#Write a Python program to sort a list of dictionaries using Lambda.

# dict=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#       {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# d=sorted(dict,key=lambda x:x['color']) #here we can compare only with the strings and always use the keyword
# print(d)

#...................................................................................................................

#decoraters are used to add features to functions as a common
# same features can be used in different functions
# decorator function will always have a inside function

#.......................................................................................................................

# TO DIVIDE (Always higher num/lower num)

# def deco(fun):
#     def wrapper(num1,num2):
#         if num1<num2:
#             num1,num2=num2,num1
#         return fun(num1,num2)
#     return wrapper
# @deco
# def div(num1,num2):
#     return num1/num2
# print(div(2,10))

#.......................................................................................................................

# to divide numbers #

# def revert_value(func):
#     def wrapper(num1,num2):
#         if num1<num2:
#             num1,num2=num2,num1  # this type of swapping is only possible in python
#         return func(num1,num2)
#     return wrapper
# @revert_value
# def sub(num1,num2):
#     return num1/num2
# print(sub(2,10))

#.......................................................................................................................

# EXCEPTION HANDELLING #
# a=[1,2,5,6,8]
# b=int(input("index"))
#
# try:
#     print(a[b])
# except Exception as e:
#     print("exception occured")
#     print(e.args)

#.......................................................................................................................















































