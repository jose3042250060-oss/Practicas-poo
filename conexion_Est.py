import mysql.connector
print("\033c")
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bd_estudiantes",
        
    )
    cursor = conexion.cursor(buffered= True)
except :
    print("por el momento no es posible conectarse a la base de datos")