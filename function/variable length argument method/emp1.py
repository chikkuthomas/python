employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

}
# def print_employee(**kwargs):# kwargs={id:1000}
#     id=kwargs['id'] #1000 here id value is taken from the kwargs dictionary
#     if id in employees: # comparing the id with the id of employees dictionary [ number]
#         print(employees[id]['name']) # if both the ids are same print the name
#     else:
#         print("invalid id")    # if not same print invalid
#     salary=kwargs['prop']
#
# print_employee(id=1000)

def print_employee(**kwargs):# kwargs={id:1000,prop:"salary"}
    id=kwargs['id'] #1000 here id value is taken from the kwargs dictionary
    prop=kwargs['prop']
    if id in employees: # comparing the id with the id of employees dictionary [ number]
        print(employees[id]['name']) # if both the ids are same print the name
        print(employees[id][prop])
    else:
        print("invalid id")    # if not same print invalid


print_employee(id=1000,prop="salary")
print_employee(id=1001,prop="designation")


#create a function print_employee() => calling fn print_employee(id=1000) - print the name of the employee

