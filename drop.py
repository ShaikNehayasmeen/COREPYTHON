import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="neha88"
)
mycursor=mydb.cursor()