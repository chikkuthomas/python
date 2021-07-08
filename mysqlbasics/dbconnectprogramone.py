#1) install package mysql -connector
#2)import msql mysql-connector
import mysql.connector

#3)establish connection
db=mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='Password@123'
)
#4)create cursor object
cursor=db.cursor()

#5)execute queries
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)

#6)close
db.close()