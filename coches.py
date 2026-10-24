class Coches:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos

    def acelerar(self):
        self._velocidad += 1

    def frenar(self):
        self._velocidad -= 1

    @property
    def velocidad(self): 
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad): 
        self._velocidad = velocidad

    @property
    def marca(self): 
        return self._marca
    @marca.setter
    def marca(self, marca): 
        self._marca = marca

    @property
    def color(self): 
        return self._color
    @color.setter
    def color(self, color): 
        self._color = color

    @property
    def modelo(self): 
        return self._modelo
    @modelo.setter
    def modelo(self, modelo): 
        self._modelo = modelo

    @property
    def potencia(self): 
        return self._potencia
    @potencia.setter
    def potencia(self, potencia): 
        self._potencia = potencia

    @property
    def asientos(self): 
        return self._asientos
    @asientos.setter
    def asientos(self, asientos): 
        self._asientos = asientos


class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos, capacidad_carga, eje):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self._capacidad_carga=capacidad_carga
        self._eje=eje
            
    def cargar(self,tipo_carga):
        print(f"El tipo de carga es:{tipo_carga}")

    def acelerar(self):
        self._velocidad+=1
        print("Estoy acelerando como un camión")

    def frenar(self):
        self._velocidad-=1
        print("Estoy frenando como un camión")

    @property
    def eje(self): 
        return self._eje
    @eje.setter
    def eje(self, eje): 
        self._eje=eje

    @property
    def capacidad_carga(self): 
        return self._capacidad_carga
    @capacidad_carga.setter
    def capacidad_carga(self, capacidad_carga): 
        self._capacidad_carga = capacidad_carga


class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos, traccion, cerrada):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self._traccion=traccion
        self._cerrada=cerrada

    def transportar(self, num_pasajeros):
        print(f"El número de pasajeros es:{num_pasajeros}")

    def acelerar(self):
        self._velocidad+=1
        print("Estoy acelerando como una camioneta")

    def frenar(self):
        self._velocidad-=1
        print("Estoy frenando como una camioneta")

    @property
    def traccion(self): 
        return self._traccion
    @traccion.setter
    def traccion(self,traccion): 
        self._traccion=traccion

    @property
    def cerrada(self): 
        return self._cerrada
    @cerrada.setter
    def cerrada(self,cerrada): 
        self._cerrada=cerrada
