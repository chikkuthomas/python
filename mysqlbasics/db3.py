#to insert into table
import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="companyy"
)
cursor=db.cursor()
sql="select *from details"
cursor.execute(sql)
result=cursor.fetchall()
for details in result:
    print(details)
db.close()