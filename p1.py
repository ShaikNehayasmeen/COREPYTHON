# import mysql.connector as c
# mydb=c.connect(
#     host="localhost",
#     user="root",
#     password="1234",
#     database="neha88"
# )
# mycursor=mydb.cursor()
#
# sql="CREATE TABLE shaik (first_name VARCHAR(50),last_name VARCHAR(50),phone_number VARCHAR(15));"
# mydb.commit()
# print("created")
# # sql="INSERT INTO customer(name,address) VALUES(%s,%s)"
# # val=("John","Highway121")
# sql_insert = "INSERT INTO shaik (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
# val = ("Shaik", "Neha", "1234567890")
# mycursor.execute(sql_insert,val)
# mydb.commit()
# print("inserted")
# sql_update = "UPDATE shaik SET phone_number = '9876543210' WHERE first_name = 'Shaik' AND last_name = 'Neha';"
# mycursor.execute(sql_update)
# mydb.commit()



