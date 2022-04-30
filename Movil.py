import math


class Movil:

    def __init__(self,velocidad,tiempo,aceleracion):
        self.velocidad=velocidad
        self.tiempo=tiempo
        self.aceleracion=aceleracion
    
    def calcular_espacio(self):
        return (2*self.velocidad) + (self.aceleracion*math.pow(self.tiempo,2))/2
def iniciar():
    try:
        velocidad=int(input("Ingrese la velocidad en m/s: "))
        tiempo=float(input("Ingrese el tiempo en segundos: "))
        aceleracion=float(input("Ingrese la aceleración en m/s: "))
        movil=Movil(velocidad,tiempo,aceleracion)
        print("El espacio recorrido es de",movil.calcular_espacio())
    except ValueError:
        print("El valor ingresado tiene que ser numérico")
iniciar()    

