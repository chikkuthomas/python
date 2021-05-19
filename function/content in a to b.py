#to move a string in a to b
def swap():
    a=input("enter the word")
    b=" "
    for i in a:
        if i not in b:
            b+=i #here dont just swap ,and each element should be added
    print(b)  #common elememt will be printed only once
swap()
