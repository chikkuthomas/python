class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee(Person):
    company="TCS"
    def __init__(self,id,salary,name,age,gender):
        super().__init__(name,age,gender)
        self.id=id
        self.salary=salary
    def details(self):
        print("company: ",Employee.company)
        print("id: ",self.id)
        print("salary: ",self.salary)

    def __str__(self):
        return str(self.age)
o=Employee(5462,50000,"Anuragh",25,"male")
o.print()
o.details()
print(o)