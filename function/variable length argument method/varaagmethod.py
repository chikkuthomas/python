# add
# def add(num1,num2):# parameters
#     return num1+num2
#
# res=add(10,20) # actuall value passes is called arguments(arg1,arg2)
# print(res)
#
# # function name
# # addThree() first calmin notation = java
# # add_three() second snake notation=python
#
# def add_three(num1,num2,num3):
#     return num1+num2+num3

# to do function with variable number of arguments
# def add(*args):
#     print(args) # always accepted as a tuple
# add(10,20)
# add(10,20,30)
# add(10,20,20)

def add(*args):
    res=0
    for num in args:
        res+=num #res=0+10+20=30
    return res #30
print(add(10,20))

def sub(*args):
    res=0
    for n in args:
        res+=n
    return res
print(sub(40,10))

#*args tuple
# **args dictionary

#keyword => value
# def print_employees(**det):
#     for k,v in det.items():
#         print(k,"=>",v)
# print_employees(id=100,place='kannur',job='engineer')

def print_employee(**kwars):
    print(kwars)
print_employee(id=1000,name="ajay",salary=50000)


