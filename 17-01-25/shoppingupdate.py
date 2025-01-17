import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="neha88"
)
mycursor = mydb.cursor()
person_id_to_update = input("Enter person_id to update: ")
new_first_name = input("Enter new first name: ")
new_last_name = input("Enter new last name: ")
new_email = input("Enter new email address: ")
sql_update = """
UPDATE shopping_person 
SET first_name = %s, last_name = %s, email = %s
WHERE person_id = %s
"""
val = (new_first_name, new_last_name, new_email, person_id_to_update)
mycursor.execute(sql_update, val)
mydb.commit()
print("Updated")
mycursor.close()
mydb.close()
