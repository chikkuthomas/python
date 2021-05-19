#age,sex,marital status(yes or no)
# then following rules print their place of
# print(service)if female work in urban
# male and age 20 to 40 work anywhere
# female only in urban areas
# age between 40 to 60 work in urban
# else print error


age=int(input("enter your age"))
sex=input("enter your sex")
marital=input("enter your marital status")
if(sex=='m')&(20<=age<=40):    #define in single quotes bcs male and female is string
    print("you can work anywhere")
elif(sex=='m')&(40<age<=60):
    print("you can work only in urban areas")
elif(sex=='f')&(age<=60):
    print("you will work only in urban areas")
else:
    print("ERROR")