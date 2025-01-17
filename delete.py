import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="neha88"
)
mycursor=mydb.cursor()
sql_delete = "DELETE from shaik where first_name='Shaik' AND last_name='Alwaz'";
mycursor.execute(sql_delete)
mydb.commit()
print("Deleted")