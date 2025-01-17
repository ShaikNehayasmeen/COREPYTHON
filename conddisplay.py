import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="neha88"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM shopping_person WHERE shipping_address = 'Khammam'")
persons = mycursor.fetchall()
if persons:
    for person in persons:
        print(person)
else:
    print("No persons found with shipping address 'Khammam'.")

mycursor.close()
mydb.close()
