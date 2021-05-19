class Student:
    def details(self,name,rollno,department,mark):
        self.name=name
        self.rollno=rollno
        self.dep=department
        self.mark=mark
        if int(mark)>190:
            print("name: ",self.name)
            print("roll no: ",self.rollno)
            print("department: ",self.dep)
            print("mark: ",self.mark)
f=open("file1","r")
for line in f:
    det=line.rstrip("\n").split(",")
    name=det[0]
    rollno=det[1]
    dep=det[2]
    # mark=int (det[3])
    mark=det[3]
    p=Student()
    p.details(name,rollno,dep,mark)
    print()

#lst.append(p)

# for i in lst:
#     if i.mark>190:
#         print(i)

# static variable defined inside class
# instance variable defined using self

# print only names- do again

