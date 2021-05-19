# inheritance class using constructor
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print(self.rollno)
        print(self.mark)
cr=Student(16,50,"Anu",14)
cr.printval()
cr.print()


