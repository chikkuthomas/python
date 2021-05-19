employees = [
    {"eid": 1000, "name": "ajay", "salary": 25000, "designation": "developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]

# print employee names only map()
e_names=list(map(lambda emp:emp['name'],employees))
# print(e_names)
# #using list
# e_name=[emp['name'] for emp in employees]
# # print("names:",e_name)
#
#
# #print all employee name into uppercase  map()
upnames=list(map(lambda name:name.upper(),e_names))
print(upnames)
#
# unames=[emp['name'].upper() for emp in employees]
# print("names:",unames)
#
#
# #print employe deatails whose name starting with 'a'   ==a  filter()
a_name=list(filter(lambda emp:emp['name'][0]=="a",employees))
print(a_name)

#
#
# #print employee details whode salary > 23000  filter()
# # e_sal=list(filter(lambda emp:emp['salary']>23000,employees))
# # print(e_sal)
#
# #list comprehension
# sal=[emp for emp in employees if emp['salary']>23000 ]
# print("employee:",sal)
#
# print employee details whose designation==developer
# e_des=list(filter(lambda emp:emp['designation']=='developer',employees))
# print(e_des)
#
# #in developers whose salary abv 24000
# dev=list(filter(lambda emp:emp['designation']=='developer' and emp['salary']>24000,employees))
# # use only "and"
# print(dev)
#
# #highest salary
# from functools import *
# highsal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
#                list(map(lambda emp:emp['salary'],employees))) # here the iterables are taken from the list of salaries
# print("highest salary:",highsal)