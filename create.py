import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="neha88"
)
mycursor=mydb.cursor()
sql_alter = "ALTER TABLE shaik ADD CONSTRAINT unique_shaik UNIQUE (first_name, last_name, phone_number);"
sql="CREATE TABLE shaik (first_name VARCHAR(50),last_name VARCHAR(50),phone_number VARCHAR(15), CONSTRAINT unique_shaik UNIQUE (first_name, last_name, phone_number));"
mydb.commit()
print("created")