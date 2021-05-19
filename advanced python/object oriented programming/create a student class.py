class Student:
    college="GCEK"       #class variable related to class
    def details(self,name,id):
        self.name=name
        self.id=id

    def print(self):
        print("Name =",self.name)
        print("id =",self.id)                # instance method s called using self
        print("College =",Student.college)   # always a class variable is called using the class name
st1=Student()
st1.details("anu",4578)
st1.print()

st2=Student()
st2.details("keerthana",478)
st2.print()

st3=Student()
st3.details("sheetal",4868)
st3.print()