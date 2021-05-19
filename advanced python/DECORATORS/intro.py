# decoraters are used to add features to a function
#decoraters are reusable functions

#design pattern: if in some project always there is a common problem we design a pattern to solve the issue

def revert_value(func):
    def wrapper(num1,num2): # same arguments as that of the function where we have to use decorator function
        if num1<num2:       # condition to be checked
            (num1,num2)=(num2,num1) # the numbers are swapped so always the highest comes first
        return func(num1,num2) # after the numbers are swapped,the nos are returned to the orginal function
    return wrapper  # return wrapper is the very first value returned

# DIVISION
@revert_value
def div(num1,num2):
    return num1/num2

# MULTIPLICATION
@revert_value
def sub(no1,no2):
    return no1-no2

print(div(2,10)) # ans will be 0.2 but here we always want higher num/lower num
print(sub(3,8))  # here we get -5,but we want 8-3=5

# while using decorator function
# 1) always the argument in decorator function is the funct of main function
# 2) there is an inner function [def wrapper]
# 3) def wrapper always has arguments same as the number of arguments in the main function
# 4) steps : when the decorater function  called
# 1)return wrapper : wrapper function is called and the output of return function has to be returned
# 2)def wrapper(num1,num2): the values from main fn, wrapeer fn method
# 3) condition statement checked
# 4) after satisying the function of the main fn method is returned
# 5) thus we get the requierd output as result: when we call the main function
# use @[ decorative function name] before every main function