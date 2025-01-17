import mysql.connector as c
try:

    mydb = c.connect(
        host="localhost",
        user="root",
        password="1234",
        database="neha88"
    )

    mycursor = mydb.cursor()
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS shopping_person (
        person_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        phone_number VARCHAR(15),
        shipping_address TEXT,
        billing_address TEXT
    );
    """
    mycursor.execute(create_table_sql)
    mydb.commit()
    print("Table 'shopping_person' created successfully.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if mydb.is_connected():
        mycursor.close()
        mydb.close()
