#print elements common in the string
def common():
    a=input("enter first string")
    b=input("enter second string")
    for i in a:
        if i in b:
            print(i)
common()
