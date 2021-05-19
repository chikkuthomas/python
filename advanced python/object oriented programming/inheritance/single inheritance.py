                # single inheritance #
# CREATING A DERIVED CLASS FROM A SUPER CLASS

# SUPER CLASS/ BASE CLASS/PARENT CLASS #
class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("name =",self.name)
        print("age =",self.age)
        print("gender =",self.gender)

      # creating a SUBCLASS/ CHILD CLASS/ DERIVED CLASS #

class Student(Person):   #calling the superclass  # calling the methods from superclass
    def print(self,department,college):
        self.department=department
        self.college=college
        print(self.department)
        print(self.college)

o=Person()
o.details("Manu",30,"male")

# object for student class #
st=Student()
st.print("EEE","GCEK")
st.details("RAHUL",22,"male")   # here we can call the method from the superclass since we have
                                # called it in the subclass

# PERSON EMPLOYEE CLASS #
class Employee(Person):
    company="TCS"
    def print(self,id,salary):
        self.id=id
        self.salary=salary
        print("company ",Employee.company)
        print("id ",self.id)
        print("salary ",self.salary)

j=Employee()
j.details("JENNA",25,"Female")
j.print(4578,30000)

