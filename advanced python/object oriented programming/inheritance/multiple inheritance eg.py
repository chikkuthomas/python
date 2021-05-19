class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Department:
    def info(self,department,place):
        self.department=department
        self.place=place
        print(self.department)
        print(self.place)

class Student(Person,Department):
    def passed(self):
        print("passed")

st=Student()
st.details("SHILPA",18,"FEMALE")
st.info("EEE","Calicut")
st.passed()
