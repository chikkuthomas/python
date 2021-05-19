class Arithmetic:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("add =",self.num1+self.num2)
        print()

    def sub(self):
        print("sub =",self.num1-self.num2)
        print()

    def mul(self):
        print("mul =",self.num1*self.num2)
        print()

    def div(self):
        print("div =",self.num1/self.num2)
        print()

o=Arithmetic(5,2)
o.add()
o.sub()
o.mul()
o.div()
