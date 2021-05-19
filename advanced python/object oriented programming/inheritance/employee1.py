class Employee:
    company="TCS"
    def __init__(self,name,age,gender,id,salary,):
        self.name=name
        self.age=age
        self.gender=gender
        self.id=id
        self.salary=salary
    def print(self):
        print(Employee.company)
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.id)
        print(self.salary)
# TWO STRING METHOD
# can use only one name
# to specify the object with a common name
    def __str__(self):
        return self.name+str(self.age)+str(self.salary)    #here we return the name of the object
e=Employee("Chitra",25,"female",4578,50000)
e.print()
print()
print(e)

# to convert int to string: "str(self.age)"