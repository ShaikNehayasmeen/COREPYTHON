import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="neha88"
)
mycursor=mydb.cursor()
mycursor.execute("select *from shaik")
shaiks=mycursor.fetchall();
for s in shaiks:
    print(s)
# mydb.commit()
print("Records fetched")