# x=10
# def printx():
#     global x  # x is made a global variable so it can be used outside the function
#     x=7
#     print(x)
# printx()    # ans x=7
# print(x)    # ans x=7
#

x=10
def printx():

    x=7  # x is made a local variable ,so it can be used only inside a function
    print(x)
printx() #and x=7
print(x)  #ans x=10