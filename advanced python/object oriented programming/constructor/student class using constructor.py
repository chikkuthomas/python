#student class
class Student:
    school="XYZ"
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def printval(self):
        print("name =", self.name)
        print("age =", self.age)
        print("id =", self.id)
        print("school =",Student.school)

o=Student("Mariya",12,457)
o.printval()

p=Student("Ram",13,1278)
p.printval()


