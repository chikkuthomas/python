# only one parent class for multiple child class

class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("name =",self.name)
        print("age =",self.age)
        print("gender =",self.gender)

        # EMPLOYEE SUB CLASS #
class Employee(Person):
    company="TCS"
    def print(self,id,salary):
        self.id=id
        self.salary=salary
        print("company ",Employee.company)
        print("id ",self.id)
        print("salary ",self.salary)
        print()

j=Employee()
j.details("JENNA",25,"Female")
j.print(4578,30000)

m=Employee()
m.details("ANUJ",30,"male")
m.print(4838,45000)
