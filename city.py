from connector import mydb

cursor=mydb.cursor()
cursor.execute("select * from customers where address='ibrahimpatnam'")
res=cursor.fetchall()
for s in res:
    print(s)