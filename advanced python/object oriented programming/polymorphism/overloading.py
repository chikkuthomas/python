class Person:
    def show(self,num1):
        self.num1=num1
        print("num1 =",self.num1)
class Student(Person):
    def show(self,num2,num3):
        self.num2=num2
        self.num3=num3
        print("num2 =",self.num2)
        print("num3 =",self.num3)
per=Student()
per.show(5,3) # only the last method will be executed , since this is not supported in python

