class Student:
    school="STS"
    def __init__(self,name,age,rollno,dep):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.dep=dep
    def print(self):
        print(self.name)
        print(self.age)
        print(self.rollno)
        print(self.dep)
    def __str__(self):    # TO CALL THE OBJECT BY A SPECIFIED ATTRIBUTE #
        return self.name + str(self.rollno)
s=Student("Manju",22,38,"EEE")
s.print()
print()
print(s)