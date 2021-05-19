#multiple parent class for one child class

class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
        
class Mobile:
    def print(self):
        print("I have 1+")
    # child class multiple inheritance #
class Child(Person,Mobile):
    def info(self,college,place):
        self.college=college
        self.place=place
        print( self.college)
        print(self.place)

per=Person()
per.details("Anu",29)

mob=Mobile()
mob.print()

ch=Child()
ch.details("Mary",30)
ch.print()
ch.info("xyz","kannur")

