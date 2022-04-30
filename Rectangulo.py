class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    
    def calcular_area(self):
        return self.base * self.altura
    
class Caja(Rectangulo):

    def __init__(self, base, altura,profundidad):
        super().__init__(base, altura)
        self.profundidad=profundidad
    
    def calcular_volumen(self):
        return self.base*self.altura*self.profundidad
def iniciar():
    try:
        base=float(input("Ingrese la medida de la base del rectángulo: "))
        altura=float(input("Ingrese la medida de la altura del rectángulo: "))
        rectangulo=Rectangulo(base,altura)
        print("El área del rectangulo es",rectangulo.calcular_area())
        profundidad=float(input("Ingrese la medida de la profundidad de la caja: "))
        caja=Caja(rectangulo.base,rectangulo.altura,profundidad)
        print("El volumen de la caja es",caja.calcular_volumen())
    except ValueError:
        print("El valor ingresado tiene que ser numérico")
iniciar()
