import mysql.connector
try:
    conexion=mysql.connector.connect(
        host='127.0.8.1',
        user='root',
        password='',
        database='bd_coches'
    )

    cursor=conexion.cursor(buffered=True)

except:
    print(f"...Por el momento, no es posible conectarse con la base de datos...\n ¡Intentelo más tarde!")
