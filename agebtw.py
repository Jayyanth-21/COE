from connector import mydb

cursor=mydb.cursor()
cursor.execute("select * from customers where age between 20 and 30")
res=cursor.fetchall()
for s in res:
    print(s)