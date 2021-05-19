# employee attributes
# name,age,id,department,salary,company

# class Employee:
#     def details(self,name,age,id,salary,department,company):
#         self.name=name
#         self.age=age
#         self.id=id
#         self.salary=salary
#         self.department=department
#         self.company=company
#     def print(self):
#         print(self.name)
#         print(self.age)
#         print(self.id)
#         print(self.salary)
#         print(self.department)
#         print(self.company)
# obj=Employee()
# obj.details("chikku",26,15478529,80000,"Engineering","TESLA")
# obj.print()

# using class variable #

class Employee:
    company_name="TELSA"
    def details(self,name,id,salary,department):
        self.name=name
        self.id=id
        self.salary=salary
        self.department=department
    def print(self):
        print(self.name)
        print(self.id)
        print(self.salary)
        print(self.department)
        print(Employee.company_name)
em1=Employee()
em1.details("anagha",4,25000,"Engineering")
em1.print()

em2=Employee()
em2.details("Manju",8,30000,"Accounting")
em2.print()

em3=Employee()
em3.details("suresh",7,32000,"Production")
em3.print()
