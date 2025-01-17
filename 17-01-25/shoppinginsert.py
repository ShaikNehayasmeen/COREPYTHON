import mysql.connector as c

try:
    # Connect to the MySQL database
    mydb = c.connect(
        host="localhost",
        user="root",
        password="1234",
        database="neha88"
    )

    # Create a cursor object
    mycursor = mydb.cursor()

    # Insert 5 records by taking user input
    for _ in range(3):  # Loop to take input for 5 persons
        print("\nEnter details for shopping person:")

        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email address: ")
        phone_number = input("Enter phone number (optional): ")
        shipping_address = input("Enter shipping address: ")
        billing_address = input("Enter billing address: ")

        # SQL Insert Statement
        sql_insert = """
        INSERT INTO shopping_person (first_name, last_name, email, phone_number, shipping_address, billing_address)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        # Values to insert
        val = (first_name, last_name, email, phone_number, shipping_address, billing_address)

        try:
            # Execute the insert query
            mycursor.execute(sql_insert, val)
            mydb.commit()
            print("Record inserted successfully.")
        except Exception as e:
            print(f"Error inserting record: {e}")
            mydb.rollback()  # Rollback in case of error

    print("5 records inserted successfully.")

except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
finally:
    # Close the cursor and connection
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
