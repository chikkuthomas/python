# DUCK TYPING: " Dynamic typing "
# importance to functionality more than class
# if it walks like a duck and quaks like a duck it must be a duck
class Pycharm:
    def compile(self): # we can pass any keyword here eg: hai,this..
        print("compile using  pycharm")
    def execute(self):
        print("execute using pycharm")
class Vscode:
    def compile(self):
        print("compile using vscode")
    def execute(self):
        print("execute using vscode")
class Person:
    def coding(self,ide):
        ide.compile()
        ide.execute()
p=Person()
pyc=Pycharm()
vsc=Vscode()
p.coding(pyc) # here we can do the function method we prefer instead of inheriting the class
            #only functionality is considered here
print()
p.coding(vsc)

