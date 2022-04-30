class Producto:

    def __init__(self,nombre,precio_costo,precio_venta):
        self.nombre=nombre
        self.precio_costo=precio_costo
        self.precio_venta=precio_venta
    
    def calcular_ganacia(self):
        return self.precio_venta-self.precio_costo
    
def iniciar():
    try:
        nombre=input("Ingrese el nombre del producto: ")
        precio_costo=float(input("Ingrese el precio de costo del producto: "))
        precio_venta=float(input("Ingrese el precio de venta del producto: "))
        if precio_costo>precio_venta:
             print("El precio de Venta debe ser mayor al precio de costo")
             exit()
        producto=Producto(nombre,precio_costo,precio_venta)
        print("El producto",producto.nombre,"tiene como ganancia",producto.calcular_ganacia())
    except ValueError:
        print("El valor ingresado tiene que ser numérico")
iniciar()


