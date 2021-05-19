#how to use attributes inside a class
#here we can use the attributes in one function(method) in another function
class Person:
    def deatils(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
obj=Person()
obj.deatils("anu",25)
obj.printval()