from connector import mydb

cursor=mydb.cursor()
cursor.execute("select * from customers order by name")
res=cursor.fetchall()
for s in res:
    print(s)