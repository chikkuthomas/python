class Parent:
    def book(self,name,author):
        self.name=name
        self.author=author
        print(self.name)
        print(self.author)
    def details(self):
        print("book is bad")

class Child(Parent):
    def details(self):
        print("book is good")
b=Child()
b.book("GHOST","Chikku")
b.details()

