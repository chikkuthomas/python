class Student:
    def print(self,name,rollno,department,mark):
        self.name=name
        self.rollno=rollno
        self.department=department
        self.mark=mark
        print("name: ",self.name)
        print("roll no: ",self.rollno)
        print("department: ",self.department)
        print("mark: ",self.mark)

    def __str__(self):
        return self.name+str(self.rollno)

f=open("file1","r")
for line in f:
    data=line.rstrip("\n").split(",")
    # print(data)
    name=data[0]
    rollno=data[1]
    department=data[2]
    mark=data[3]

    st=Student()
    st.print(name,rollno,department,mark)
    print(st)
    print()

# to print details of student having mark >190