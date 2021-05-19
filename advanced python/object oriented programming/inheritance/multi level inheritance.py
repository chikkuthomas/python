#multi level inheritance,where each class is inherited as alevel

class Employee:
    company="TCS"
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print("age :",self.age)
        print(self.gender)
        print("company : ",Employee.company)

class Dep(Employee):
    def info(self,department,salary):
        self.department=department
        self.salary=salary
        print("department :",self.department)
        print("salary :",self.salary)

class Person(Dep):
    def per(self):
        print("good worker")
c=Person()
c.details("Ram",28,"male")
c.info("IT",40000)
c.per()
