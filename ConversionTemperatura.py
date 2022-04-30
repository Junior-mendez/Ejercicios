class ConversionTemperatura:
    temperatura=0

    def __init__(self,temperatura):
        self.temperatura=temperatura
    
    def calcular_farenheit(self):
        return (self.temperatura*9/5)+32

def iniciar():
    try:
        grados=float(input("Ingrese el valor de grados en centígrados: "))
        conversion=ConversionTemperatura(grados)
        farenheit=conversion.calcular_farenheit()
        print("Grados en farenheit:",farenheit)
    except ValueError:
        print("El valor ingresado tiene que ser numérico")

iniciar()