from conexionBD import conexion, cursor

class CochesBD:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos

    def insertar(self):
        try:
            cursor.execute(
                "INSERT INTO coches VALUES (NULL, %s, %s, %s, %s, %s, %s)",(self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar coche: {e}")
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM coches")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar coches: {e}")
            return []
        
    @staticmethod
    def eliminar( id):
        try:
            cursor.execute("DELETE FROM coches WHERE id=%s", (id,))
            conexion.commit()
            return True
        except :
            print(f"Error al eliminar coche ")
            return False

    @staticmethod
    def actualizar(self, id):
        try:
            cursor.execute(
                "UPDATE coches SET marca=%s, color=%s, modelo=%s, velocidad=%s, potencia=%s, asientos=%s WHERE id=%s",(self._marca, self._color, self._modelo, self._velocidad, self._potencia, self._asientos, id))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar coche: {e}")
            return False