#to initialise instance variables (only)
#constructor automatically invoke when creating object
#we can give values while creating objects
# for one constructor only one method
class Person:
    def __init__(self,name,age,gender):  #(constructor is __init__)
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.gender)
per=Person("MARIA",23,"female")   #here we can give the values withot calling the method
per.printval()