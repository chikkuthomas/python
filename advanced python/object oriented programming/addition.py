# addition program using oop
class Addition:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2


    def sum(self):
        print("sum =",self.num1 + self.num2) # calling the variable using sel
o=Addition()
o.add(10,20)
o.sum()

s=Addition()
s.add(75,68)
s.sum()