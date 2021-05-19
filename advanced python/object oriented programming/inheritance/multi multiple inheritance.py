# person, student, parent, child
# parent inherit person
#child class inherit person
# student =child

class Person:
    def details(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
        print(self.name)
        print(self.gender)
        print("age:",self.age)
class Parent(Person):
    def info(self,job,type):
        self.job=job
        self.type=type
        print("job:",self.job)
        print("job type:",self.type)
class Child(Person):
    def child(self,school,division):
        self.school=school
        self.division=division
        print("school:",self.school)
        print("division:",self.division)
class Student(Child):
    def print(self,location):
        self.location=location
        print(self.location)

o=Person()
o.details("Nithya",25,"female")
print()

p=Parent()
p.details("anu",24,"female")
p.info("teacher","full time")
print()

c=Child()
c.details("manu",15,"male")
c.child("xyz",10)
print()

s=Student()
s.details("Ramesh",12,"male")
s.child("GVS",7)
s.print("kannur")
print()


