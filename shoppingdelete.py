import mysql.connector as c


mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="neha88"
)


mycursor = mydb.cursor()


person_id_to_delete = input("Enter person_id to delete: ")


sql_delete = "DELETE FROM shopping_person WHERE person_id = %s"
val = (person_id_to_delete,)


mycursor.execute(sql_delete, val)
mydb.commit()
if mycursor.rowcount > 0:
    print(f"Record with person_id {person_id_to_delete} deleted successfully.")
else:
    print(f"No record found with person_id {person_id_to_delete}.")


mycursor.close()
mydb.close()
