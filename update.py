from connector import mydb

cursor=mydb.cursor()
cursor.execute("update customers set name='jai' where address='l.b nagar'")
mydb.commit()