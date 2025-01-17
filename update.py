import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="neha88"
)
mycursor=mydb.cursor()
sql_update = "UPDATE shaik SET phone_number = '9876543210' WHERE first_name = 'Shaik' AND last_name = 'Neha';"
mycursor.execute(sql_update)
mydb.commit()
print("Updated")