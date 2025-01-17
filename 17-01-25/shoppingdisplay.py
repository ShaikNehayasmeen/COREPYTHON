import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="neha88"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM shopping_person")
persons = mycursor.fetchall()
for person in persons:
    print(person)
mycursor.close()
mydb.close()
