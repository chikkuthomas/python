import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="companyy"
)
cursor=db.cursor()
sql="create table location(lid varchar(25),location_name varchar(25))"
cursor.execute(sql)
db.close()