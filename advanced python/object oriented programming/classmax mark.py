# #Create objects of the following file and print the details of student
# # with maximum mark? anu,1,bca,200 rahul,2,bba,177 vinod,3,bba,187 ajay,4,bca,198 maya,5, bba,195
#
# class Student:
#     def details(self,name,rollno,department,mark):
#         self.name=name
#         self.roll=rollno
#         self.dep=department
#         self.mark=mark
#         print("NAME: ",self.name)
#         print("ROLL NO: ",self.roll)
#         print("DEPARTMENT: ",self.dep)
#         print("MARK: ",self.mark)
# f=open("mark","r")
# lst=[]
# for line in f:
#     data=line.rstrip("\n").split(",")
#     lst.append(data)#[[anu,1,bca,200],[rahul,2,bba,177],[vinod,3,bba,187],[ajay,4,bca,198],[maya,5, bba,195]
# print(lst)
# for i in range(0,len(lst)):#(0,5) i=0       1       2     3
#     for j in range(0,len(lst)-i-1):#j=(0,4)  (0,3)  (0,2)  (0,1)
#         if lst[j][-1]>lst[j+1][-1]:
#             temp = lst[j]
#             lst[j] = lst[j + 1]
#             lst[j + 1] = temp
# name=lst[-1][0]
# roll=lst[-1][1]
# dep=lst[-1][2]
# mark=lst[-1][3]
#
# print("details of student with maximum mark")
# o=Student()
# o.details(name,roll,dep,mark)

class Student:
    def __init__(self,name,rollno,dep,mark):
        self.name=name
        self.rollno=rollno
        self.dep=dep
        self.mark=mark
    def print(self):
        print(self.name)
        print(self.rollno)
        print(self.dep)
        print(self.mark)
f=open("mark","r")
l=[]
for i in f:
    d=i.rstrip("\n").split(",")
    name=d[0]
    rollno=d[1]
    dep=d[2]
    mark=d[3]
    st=Student(name,rollno,dep,mark)
    l.append(st.mark)
    if(st.mark==max(l)): # comparing each element with the max mark in the mark list
        print(st.name,st.rollno,st.dep,st.mark) # printing the details of the student with max mark