import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="companyy"
)
cursor=db.cursor()

sql="select *from location"

cursor.execute(sql)

result=cursor.fetchall() #get all results to location pycharm

for location in result: #iterating result
    print(location)     #printing

db.close()

