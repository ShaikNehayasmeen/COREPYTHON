import mysql.connector as c
try:

    mydb = c.connect(
        host="localhost",
        user="root",
        password="1234",
        database="neha88"
    )


    mycursor = mydb.cursor()
    for _ in range(3):
        print("\nEnter details for shopping person:")

        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email address: ")
        phone_number = input("Enter phone number (optional): ")
        shipping_address = input("Enter shipping address: ")
        billing_address = input("Enter billing address: ")
        sql_insert = """
        INSERT INTO shopping_person (first_name, last_name, email, phone_number, shipping_address, billing_address)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        val = (first_name, last_name, email, phone_number, shipping_address, billing_address)

        try:

            mycursor.execute(sql_insert, val)
            mydb.commit()
            print("Record inserted successfully.")
        except Exception as e:
            print(f"Error inserting record: {e}")
            mydb.rollback()

    print("5 records inserted successfully.")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
finally:

    if mydb.is_connected():
        mycursor.close()
        mydb.close()
