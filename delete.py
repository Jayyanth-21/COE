from connector import mydb

cursor=mydb.cursor()
cursor.execute("delete from customers where name='hrushi'")
mydb.commit()