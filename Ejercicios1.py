# #Calcular el salario neto de un trabajador. Se debe leer el nombre, horas trabajadas, precio de la hora y sabiendo que los impuestos aplicados son el 10 por ciento sobre el salario bruto. sb = ph * htsn = sb - 0.10 * sb
# nombre= input("Ingrese el nombre: ")
# salarioNeto = float(input("Ingrese las horas trabajadas: "))
# precioHora = float(input("Ingrese el monto por hora: "))
# salarioBruto=precioHora*salarioNeto
# salarioNeto =  salarioBruto - 0.10 * salarioBruto
# print("El salario neto es",salarioNeto)


# ##Ejercicio 1: Hacer un programa para que se ingresen 2 números y reporte su suma, resta y multiplicación.
# num1= int(input("Ingresa el primer número: "))
# num2= int(input("Ingresa el primer número: "))
# suma= num1+num2
# resta=num1-num2
# mult= num1*num2
# print("Suma:",suma)
# print("Resta:",resta)
# print("Multiplicación:",mult)

# ##Ejercicio 2: Calcular la altura que cae un objeto. Se debe ingresar el tiempo recorrido en segundos. H = 0.5 * G * T 2  G = 9.8 m/seg2
# tiempo=int(input("Ingrese el tiempo en segundos: "))
# gravedad = 9.8
# altura=0.5*gravedad*tiempo
# print("La altura es:",altura,"metros")

# ##Ejercicio 3: La gaseosa en la planta embotelladora se almacena en tanques cilíndricos de un radio de 2 metros. 
# #Se necesita un programa que ingresando la altura hasta la que llega la gaseosa, calcule el volumen 
# #que se tiene.
# #(Volumen del cilindro = Pi * radio2* altura)
# import math
# altura=float(input("Ingrese la altura: "))
# volumen=math.pi*2*altura
# print("El volumen del tanque es",volumen,"metros cúbicos")


# ###Ejercicio 4: Una empresa paga a sus vendedores un sueldo básico mensual de S/.300. El sueldo bruto es 
# #igual al sueldo básico más una comisión, que es igual al 9% del monto total vendido. Por ley, 
# # todo vendedor se somete a un descuento del 11 %. Diseñe un programa que calcule la comisión, 
# # el sueldo bruto, el descuento y el sueldo neto de un vendedor de la empresa. Se debe ingresar el 
# # monto total vendido
# totalVendido=float(input("Ingrese el total vendido: "))
# sueldoBasico=300
# comision=0.09*totalVendido
# sueldoBruto=sueldoBasico+comision
# descuento=0.11*sueldoBruto
# sueldoNeto=sueldoBruto-descuento
# print("Comsision obtenida por el vendedor:",comision," soles")
# print("Sueldo Bruto del vendedor:",sueldoBruto," soles")
# print("Descuento realizado al vendedor:",descuento," soles")
# print("Sueldo Neto del Vendedor:",sueldoNeto," soles")


# ##Ejercicio 5:La distancia entre dos puntos (x1, y1) y (x2, y2) de un plano se puede obtener sacando la raíz 
# # # cuadrada de la expresión (x2 – x1)2 + (y2 – y1)2
# # # . Escribir un programa que, dados dos puntos 
# # # por el usuario, calcule la distancia entre estos dos puntos.

# import math
# print("Informacion primer punto: ")
# x1=float(input("Ingrese el punto X1: "))
# y1=float(input("Ingrese el punto Y1: "))
# print("Informacion segundo punto: ")
# x2=float(input("Ingrese el punto X2: "))
# y2=float(input("Ingrese el punto Y2: "))

# distancia = math.sqrt(((x2-x1)**2) + (y2-y1)**2)
# print(distancia)

# # # Ejercicio 6: Dada una cantidad de dinero en soles, diseñe un programa que descomponga dicha cantidad en 
# # # billetes de S/. 100, S/. 50, S/.10 y monedas de S/. 5, S/. 2 y S/.1. Así, por ejemplo, S/. 3778 
# # # puede descomponerse en 37 billetes de S/. 100, más 1 billete de S/. 50, más 2 billetes de S/. 10, 
# # # más 1 moneda de S/. 5, más 1 moneda de S/.2 y más 1 moneda de S/. 1.

# monto=int(input("Ingrese el monto a descomponer: "))

# cantidad100= int(monto/100)
# cantidad50 = int(monto%100/50)
# cantidad10 = int(monto%100%50/10)
# cantidad5  = int(monto%100%50%10/5)
# cantidad2  = int(monto%100%50%10%5/2)
# cantidad1  = int(monto%100%50%10%5%2/1)
# print("Cantidad S/ 100:",cantidad100)
# print("Cantidad S/ 50:",cantidad50)
# print("Cantidad S/ 10:",cantidad10)
# print("Cantidad S/ 5:",cantidad5)
# print("Cantidad S/ 2:",cantidad2)
# print("Cantidad S/ 1:",cantidad1)

# # # Ejercicio 7: Dado un número natural de cuatro cifras, diseñe un algoritmo que forme un número con la cifra 
# # # de los millares y la cifra de las unidades, en ese orden. Así, por ejemplo, si se ingresara el número 
# # # 8235, el número formado sería 85.

# numero= int(input("Ingrese un numero de cuatro dígitos: "))
# numero1=int(numero/1000)
# numero2=int(numero%1000%100%10)
# numeroformado=numero1*10+numero2
# print("Numero formado", numeroformado)

# # # Ejercicio 8: Dado un número natural de tres cifras, diseñe un algoritmo que permita obtener el revés del 
# # # número. Así, si se ingresa el número 238 el revés del número es 832.

# numero= int(input("Ingrese un número de tres cifras: "))
# cifra1=int(numero/100)
# cifra2=int(numero/10%10)
# cifra3=int(numero%10)
# print("El numero al revés es: ",cifra3*100+cifra2*10+cifra1)


# # # Ejercicio 9: Construya una aplicación que determine cuanto se le debe cobrar a los clientes de un grifo, dado 
# # # que los surtidores registran lo que venden en galones, pero el precio de la gasolina está fijado en 
# # # litros. Cada galón tiene 3.785 litros. El precio del litro es S/ 3.86.

# cantidadGalones=float(input("Ingrese la cantidad de galones vendidos: "))
# vendido=cantidadGalones*3.785*3.86
# print("El monto a cobrar  es: ",vendido)


# # # Calcular el interés generado por un capital depositado durante cierta cantidad de períodos a una 
# # tasa de interés determinada y expresada en porcentaje.
# # Aplicar las siguientes fórmulas:
# # i. Monto = Capital*(1 + tasa/100) Número Períodos
# # # ii. Interés = Monto – Capital

# capital=float(input("Ingrese el monto del capital: "))
# tasa=float(input("Ingrese el monto de la tasa: "))
# periodos=int(input("Ingrese la cantidad de periodos: "))
# monto=capital*(1 + tasa/100)**periodos
# interes=monto-capital
# print("El interés generado es",interes)