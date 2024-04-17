from mysql.connector import Error, connect

try:
    connection = connect(
        host='172.16.5.4',
        port=3310,
        user='root',
        password='root',
        database='ecommerce' 
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("""""")
        connection.commit()  # Se debe realizar un commit después de ejecutar la consulta
except Error as ex:
    print("Error during connection:", ex)
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()  # Se debe cerrar el cursor
        connection.close()
        print("Connection closed.")