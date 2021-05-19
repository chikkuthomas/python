#in python line by line execution of code

#here the error comes in the input so give it inside the try block
#considering the code try and except block work together
try:
    a = int(input("num1"))
    b = int(input("num2"))
    print(a/b)
except:
    print("please enter an integer value")
finally:
    print("done")