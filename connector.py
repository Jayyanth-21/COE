import mysql.connector as mc

mydb=mc.connect(
    host="localhost",
    port=3310,
    user="root",
    password="root",
    database="db"
)
