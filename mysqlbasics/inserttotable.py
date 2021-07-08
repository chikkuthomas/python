import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="companyy"
)
cursor=db.cursor()
sql="insert into location(lid,location_name) values('1','ekm'),('2','ktm'),('3','wyd'),('4','tcr'),('5','pkd'),('6','tvm')"
cursor.execute(sql)
db.commit() #to give the result to mysql
db.close()