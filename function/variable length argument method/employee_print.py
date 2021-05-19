#create a function print_employee() => calling fn print_employee(id=1000) name of that employee
employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

}
def print_employee(**kwargs): #dict format= {id:1000,prop:"salary}
    id=kwargs['id'] # we use double quotes to call the keyword
    prop=kwargs['prop']
    if id in employees:
        print(employees[id]['name'])
        print(employees[id][prop])

print_employee(id=1000,prop='salary') # name, salary
print()
print_employee(id=1002,prop='designation')

