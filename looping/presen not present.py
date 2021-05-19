# in a string if a letter is present print present if not print not present
def present():
    flag=0
    a=input("enter the letter")
    for val in "luminar":
        if val in a:
            flag=1
    if(flag>0):
        print("present")
    else:
        print("not present")


present()
