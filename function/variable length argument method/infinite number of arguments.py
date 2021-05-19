# variable length argument method is used to add ariable number of arguments while
# a function method is called
#by using variable argument method we can add different number of arguments while calling the function method

# def add(num1,num2) here num1 and num2 are "PARAMETERS"
# add(10,20) here the 10 and 20 are "ARGUMENTS"

#in def add(num1,num2) = here we can do the function method only with 2 arguments
# we need to call another fuction for 3 arguments to do the same operation

# so inorder to tackle this we use the "VARIABLE ARGUMENT METHOD"
# we use *args - which means even if there is zero arguments or n number of arguments no problem
# (instead of args we can use any word)

# *args will accept any number of arguments

#eg.1
# ADD NUMBERS
def add(*args):
    sum=0
    for n in args: #to iterate each element in the argumenst
        sum+=n #to add each numbers and find the sum
    print("total sum:",sum)
    print(type(args))  # to know the type of arguments = tuple

# CALLING FUNCTION METHOD WITH ARGUMENTS #
add(10,20)
add(10,20,30)
add(30,40,50,60,45)

# how many arguments we pass the type of args will be a tuple [tuple format ]


