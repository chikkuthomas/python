#object oriented programming-where object is created

# class: design pattern
# object: real world entity
# reference: name that refers a memory location of a object

## TO CREATE A CLASS ##
class Person:   #always use a word with first capital - standard form to define a class
    def walk(self):#(self) is beacuse we are giving fn inside a class,class includes methods
        print("person is walking")
    def jump(self):
        print("person is jumping")

# self is an instance variable  and is related to methods


obj=Person()   #here object is the reference and here the memory is allocated
obj.walk()
obj.jump()

obj1=Person()  # we can create diff number of reference
obj1.walk()
obj1.jump()

