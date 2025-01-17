import mysql.connector as c
import display

mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="neha88"
)
mycursor=mydb.cursor()
first_name=("Enter your firstname")
last_name=("Enter your lastname")
phone_number=("Enter your phonenumber")
sql_insert = "INSERT INTO shaik (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
val =(first_name,last_name,phone_number)
mycursor.executemany(sql_insert,val)
mydb.commit()''
print("inserted")