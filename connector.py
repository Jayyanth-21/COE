import mysql.connector as mc

mydb=mc.connect(
    host="localhost",
    port=3310,
    user="root",
    password="root",
    database="db"
)
cursor=mydb.cursor()
name=input("enter the name")
address=input("enter the address")
query="insert into customers values(%s,%s)"
cursor.execute(query,(name,address))
mydb.commit()