import math


class TrianguloRectangulo:
    cateto1=0
    cateto2=0
    def __init__(self,cateto1,cateto2) :
        self.cateto1=cateto1
        self.cateto2=cateto2
    def calcular_area(self):
        return (self.cateto1*self.cateto2)/2
    def calcular_hipotenusa(self):
        return math.sqrt(math.pow(self.cateto1,2)+math.pow(self.cateto2,2))
    def calcular_permitro(self):
        return self.cateto1+self.cateto2+self.calcular_hipotenusa()

def iniciar():
    try:
        cateto1=float(input("Ingresa la medida del cateto 1: "))
        cateto2=float(input("Ingresa la medida del cateto 2: "))
        triangulo = TrianguloRectangulo(cateto1,cateto2)
        area=triangulo.calcular_area()
        print("Area:",area)
        hipotenusa=triangulo.calcular_hipotenusa()
        print("Hipotenusa:",round(hipotenusa,2))
        permitetro=triangulo.calcular_permitro()
        print("Perímetro:",round(permitetro,2))
    except ValueError:
        print("El valor ingresado tiene que ser numérico")
iniciar()







