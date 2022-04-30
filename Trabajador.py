class Trabajador:

    def __init__(self,nombre,precio_hora,horas_trabajadas):
        self.nombre=nombre
        self.precio_hora=precio_hora
        self.horas_trabajadas=horas_trabajadas
    
    def calcular_salario(self):
        return self.precio_hora*self.horas_trabajadas
    
    def calcular_impuesto(self):
        return self.calcular_salario()*0.1
    
    def calcular_neto(self):
        return self.calcular_salario() - self.calcular_impuesto()
def iniciar():
    try:
        nombre=input("Ingrese el nombre del trabajador: ")
        precio_hora=float(input("Ingrese el precio de costo del producto: "))
        horas_trabajadas=int(input("Ingrese el precio de venta del producto: "))
        trabajador=Trabajador(nombre,precio_hora,horas_trabajadas)
        print("El trabajador",trabajador.nombre,"tiene un sueldo neto de",trabajador.calcular_neto(),"soles")
    except ValueError:
        print("El valor ingresado tiene que ser numérico")
iniciar()



