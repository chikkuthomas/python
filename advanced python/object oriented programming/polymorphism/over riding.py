#child class method will override the parent class method
class Parent:
    def properties(self):
        print("10 lakh rs, 2 cars")
    def marry(self):
        print("with ram")
class Child(Parent):
    def marry(self):
        print("with rahul")
c=Child()
c.properties()
c.marry()   # since the child and parent has same method only child will be executed