from connector import mydb

cursor=mydb.cursor()
cursor.execute("select * from customers")
rec=cursor.fetchall()
for s in rec:
    print(s)