class Parent:
    def print(self,name,age):
        self.name=name
        self.age=age
        print("name: ",self.name)
        print("age: ",self.age)
o=open("file","r")
lst=[]
for line in o:
    data=line.rstrip("\n").split(",")   #.rstrip("/n") - to strip the list
    # print(data) # here since each one is in different line, it will be added as different list
    name=data[0]
    age=data[1]
    p=Parent()
    p.print(name,age)
    print()