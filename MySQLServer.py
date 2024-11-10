import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='mistir',  
        password='123456'  
    )

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()