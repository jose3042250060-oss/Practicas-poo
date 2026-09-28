"""
Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado

def areaREctangulo(altura,base):
    area=altura*base
    return area
res="si"
while res=="si":
    print("\033c")
    altura=float(input("Ingrese un la altura del rectangulo:.."))
    base=float(input("Ingrese un la base del rectangulo:..."))

    area1 = areaREctangulo(altura, base)
    print(f"El area es:..{area1}")
    
    res=input("Deseas calcular de nuevo (si/no):...").lower()
    while res!="si" and res!="no":
        res=input("Deseas calcular de nuevo (si/no):...").lower()

print("\033c")
print("\nEspero haberte ayudado")

#Implementar el paradigma Orientado a Objetos (OO)

class Rectangulos:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

rect = Rectangulos(5, 3)
print(rect.area())


class Rectangulos:
    def area (self,base,altura):
        areaR=base*altura
        return areaR


Rectangulo1=Rectangulos()
print(f"El area del rectangulo es: {Rectangulo1.area(5,6)}")