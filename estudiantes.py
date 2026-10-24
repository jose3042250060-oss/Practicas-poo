from conexion_Est import conexion, cursor

class Estudiantes:
    def __init__(self, nombre, nota):
        self._nombre =  nombre 
        self._nota = nota
    @property
    def nombre(self):
        return self._nombre
    @property
    def nota(self):
        return self._nota
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre 
    @nota.setter
    def nota(self,nota):
        self._nota = nota 

    def insertar(self):
        try:
            cursor.execute("INSERT INTO estudiantes VALUES (NULL, %s, %s)",(self._nombre,self._nota))
            conexion.commit()
            return True
        except:
        
            return False
    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from estudiantes")
            return cursor.fetchall()
        except:
            
            return[]
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("delete  from estudiantes where id=%s",(id,))
            conexion.commit()
            return True
        except:
            return False 

    def actualizar(self,id):
        try:
            cursor.execute("update estudiantes set nombre = %s, nota = %s where id = %s",(self._nombre,self._nota, id))
            conexion.commit()
            return True
        except Exception as e:
            print("Error al actualizar:..",e)
            return False