import math


class ObjetoGeometrico:
    def __init__(self,valorx,valory):
        self.valorx=valorx
        self.valory=valory
    

class Circulo(ObjetoGeometrico):
    def __init__(self, valorx, valory,radio):
        super().__init__(valorx, valory)
        self.radio=radio

    def calcular_area(self):
        return math.pi*math.pow(self.radio,2)

class Cuadrado(ObjetoGeometrico):
    def __init__(self, valorx, valory,lado):
        super().__init__(valorx, valory)
        self.lado=lado
    
    def calcular_area(self):
        return math.pow(self.lado,2)
def iniciar():
    try:
        valorx=int(input("Ingrese el valor de 'X' de círculo: "))
        valory=int(input("Ingrese el valor de 'Y' de círculo: "))
        radio=float(input("Ingrese la medida del radio del círculo: "))
        circulo=Circulo(valorx,valory,radio)
        print("El área del circulo es",circulo.calcular_area())
        print("El centro del circulo es","x:",circulo.valorx,", y:",circulo.valory)

        valorx=int(input("Ingrese el valor de 'X' del cuadrado: "))
        valory=int(input("Ingrese el valor de 'Y' del cuadrado: "))
        lado=float(input("Ingrese la medida del lado del cuadrado: "))
        cuadrado=Cuadrado(valorx,valory,lado)
        print("El área del cuadrado es",cuadrado.calcular_area())
        print("El centro del cuadrado es","x:",cuadrado.valorx,", y:",cuadrado.valory)
    except ValueError:
        print("El valor ingresado tiene que ser numérico")
iniciar()

