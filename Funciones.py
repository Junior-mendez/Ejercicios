# # 1) Calcular la altura que cae un objeto. Se debe ingresar el tiempo recorrido en segundos. 
# # (H = 0.5 * G * T 2
# # . G = 9.8 m/seg2)
# def calcular_altura(tiempo):
#     altura=0.5*9.8*tiempo**2
#     print("La altura es",round(altura,2),"metros")
# tiempo=float(input("Ingrese el tiempo en segundos: "))
# calcular_altura(tiempo)

# # 2) Calcular Monto generado por un capital depositado durante cierta cantidad de períodos 
# # a una tasa de interés determinada y expresada en porcentaje.
# # Monto = Capital*(1 + tasa/100)NumeroPeríodo
# def calcular_monto(capital,periodos,tasa):
#     monto=capital*(1+tasa/100)**periodos
#     print("El monto es",round(monto,2))
# capital=float(input("Ingrese el monto del capital: "))
# periodos=float(input("Ingrese la cantidad de periodos: "))
# tasa=float(input("Ingrese la tasa en base a 100%: "))
# calcular_monto(capital,periodos,tasa)

# # 3) Calcular el volumen de un cilindro dada el radio y la altura.
# import math
# def calcular_volumen(radio,altura):
#     volumen = math.pi * radio**2 * altura
#     print("El volumen es",round(volumen,2),"cm")
# radio=float(input("Ingrese el radio del cilindro en cm: "))
# altura=float(input("Ingrese la altura del cilindro en cm: "))
# calcular_volumen(radio,altura)


# # 4) Ingrese un número que represente segundos y determinar a cuanto equivale en horas, 
# # minutos y segundos.
# # Ejemplo: Si se ingresa 9500 segundos el programa debería reportar: 2 horas, 38 
# # minutos y 20 segundos.
# def calcular(segundoscantidad):
#     if segundoscantidad>0:
#         horas=segundoscantidad//3600
#         horasresiduo=segundoscantidad%3600
#         print(horas,"horas")
#         minutos=horasresiduo//60
#         minutosresiduo=horasresiduo%60
#         print(minutos,"minutos",)
#         segundos=minutosresiduo%60
#         print(segundos,"segundos")
# segundos=int(input("Ingrese la cantidad de segungos: "))
# calcular(segundos)

# # 5) Calcule el valor de la función Fx, dada por 
# #  x
# # 3
# # + x/2, para x < 0
# # Fx = 
# #  4x2
# # – 2 , para x ≥ 0
# def calcular_funcion(valorx):
#     if valorx<0:
#         funcion=valorx**3+valorx/2
#     else:
#         funcion=4*valorx**2-2
#     print("El valor de la función es",round(funcion,2))
# valorx=float(input("Ingrese el valor de x: "))
# calcular_funcion(valorx)

# # 6) En el curso de Algoritmos se rinden 4 exámenes de las cuales se elimina la menor nota. 
# # Hacer un programa para ingresar las notas de los 4 exámenes y reportar la nota 
# # eliminada y el promedio final del alumno
# def ingresar_notas():
#     notas=[]
#     suma=0
#     for i in range(4):
#         nota=int(input("Ingrese la nota: "))
#         notas.append(nota)
#         suma=suma+nota
#     notas.sort()
#     promedio=(suma-notas[0])/3
#     nota=notas.pop(0)
#     print("Nota eliminada:",nota)
#     print("Promedio:",promedio)
# ingresar_notas()

# # 7) Ingresar 3 números y reportar el menor de ellos
# def numero_menor(numeros):
#     numeros.sort()
#     print("El numero menor es",numeros[0])
# def ingresar_numero():
#     numeros=[]
#     print("######## Ingrese tres números ############")
#     for i in range(3):
#         numero= int(input("Ingrese el número: "))
#         numeros.append(numero)
#     numero_menor(numeros)
# ingresar_numero()

# # 8) Diseñe un programa que determine le categoría de un estudiante en base a su promedio 
# # ponderado de acuerdo a la siguiente tabla:
# # PROMEDIO CATEGORIA
# # >=17 A
# # >=14 pero <17 B
# # >=12 pero <14 C
# # < 12 D
# def determinar_categoria(nota):
#     if nota>=17:
#         print("Categoría A")
#     if nota>=14 and nota<17:
#         print("Categoría B")
#     if nota>=12 and nota<14:
#         print("Categoría C")
#     if nota<12:
#         print("Categoría D")
# nota=int(input("Ingrese el promedio: "))
# determinar_categoria(nota)

# # 9) Ingresar el día y el mes de nacimiento y reportar su signo zodiacal.
# def signo(dia_nacimiento, mes_nacimiento):
#     if mes_nacimiento == 1:
#         if dia_nacimiento <= 20:
#             signo = "Capricornio"
#         else:
#             signo = "Acuario"
#     elif mes_nacimiento == 2:
#         if dia_nacimiento <= 18:
#             signo = "Acuario"
#         else:
#             signo = "Piscis"
#     elif mes_nacimiento == 3:
#         if dia_nacimiento <= 20:
#             signo = "Piscis"
#         else:
#             signo = "Aries"
#     elif mes_nacimiento == 4:
#         if dia_nacimiento <= 20:
#             signo = "Aries"
#         else:
#             signo = "Tauro"
#     elif mes_nacimiento == 5:
#         if dia_nacimiento <= 21:
#             signo = "Tauro"
#         else:
#             signo = "Géminis"
#     elif mes_nacimiento == 6:
#         if dia_nacimiento <= 21:
#             signo = "Géminis"
#         else:
#             signo = "Cáncer"
#     elif mes_nacimiento == 7:
#         if dia_nacimiento <= 22:
#             signo = "Cáncer"
#         else:
#             signo = "Leo"
#     elif mes_nacimiento == 8:
#         if dia_nacimiento <= 23:
#             signo = "Leo"
#         else:
#             signo = "Virgo"
#     elif mes_nacimiento == 9:
#         if dia_nacimiento <= 23:
#             signo = "Virgo"
#         else:
#             signo = "Libra"
#     elif mes_nacimiento == 10:
#         if dia_nacimiento <= 23:
#             signo = "Libra"
#         else:
#             signo = "Escorpio"
#     elif mes_nacimiento == 11:
#         if dia_nacimiento <= 22:
#             signo = "Escorpio"
#         else:
#             signo = "Sagitario"
#     elif mes_nacimiento == 12:
#         if dia_nacimiento <= 21:
#             signo = "Sagitario"
#         else:
#             signo = "Capricornio"
#     print("su signo es",signo)
# dia=int(input("Indique el día de su nacimiento: "))
# mes=int(input("Indique el mes de su nacimiento: "))
# signo(dia,mes)

# # 10) Ingresar el día y el mes de una fecha y reportar la estación a la que pertenece: verano, 
# # otoño, invierno o primavera.
# def estacion(dia,mes):
#     if mes==1 or mes==2:
#         estacion="Verano"
#     elif mes==4 or mes==5:
#         estacion="Otoño"
#     elif mes==7 or mes==8:
#         estacion="Invierno"
#     elif mes==10 or mes==11:
#         estacion="Primavera"
#     elif mes==3:
#         if dia<=20:
#             estacion="Verano"
#         else:
#             estacion="Otoño"
#     elif mes==6:
#         if dia<=21:
#             estacion="Otoño"
#         else:
#             estacion="Invierno"
#     elif mes==9:
#         if dia<=22:
#             estacion="Invierno"
#         else:
#             estacion="Primavera"
#     elif mes==12:
#         if dia<=21:
#             estacion="Primavera"
#         else:
#             estacion="Verano"
#     print(estacion)
# dia=int(input("Indique el día: "))
# mes=int(input("Indique el mes: "))
# estacion(dia,mes)

# # 11) Ingresar 2 números y luego un carácter indicando la operación a realizar (+,-,*,/,^) y 
# # reportar el resultado de la operación
# def operacion(numero1,numero2,operacion):
#     if operacion=="*":
#         resultado=numero1*numero2
#     elif operacion=="/":
#         resultado=numero1/numero2
#     elif operacion=="+":
#         resultado=numero1+numero2
#     elif operacion=="-":
#         resultado=numero1-numero2
#     elif operacion=="^":
#         resultado=numero1**numero2
#     print("El resultado de la operacion es",resultado)
# numero1=int(input("Ingrese el primer numero: "))
# numero2=int(input("Ingrese el segundo numero: "))
# simbolo=input("Ingrese el simbolo de la operación a realizar(+,-,*,/,^): ")
# operacion(numero1,numero2,simbolo)

# # 12) Ingresar un numero entero y reportar si es perfecto o no. Un numero es perfecto 
# # cuando es igual a la suma de divisores menores que el.
# def numero_perfecto(numero):
#   suma = 0
#   for i in range(1,numero):
#     if (numero % i == 0):
#       suma += i
#   if numero == suma:
#      print(numero,"es un numero perfecto")
#   else:
#     print(numero,"no es un numero perfecto")
# numero = int(input("introduzca un numero:"))
# numero_perfecto(numero)

# # 13) Ingresar 2 números y reportar su mínimo común múltiplo
# def mcd(numero1,numero2):
#     mayor=max(numero1,numero2)
#     menor=min(numero1,numero2)
#     while menor:
#         temporal=menor
#         menor=mayor%menor
#         mayor=temporal
#     return temporal
# def mcm(numero1,numero2):
#     minimocomun=(numero1*numero2)//mcd(numero1,numero2)
#     print("El mínimo común múltiplo es",minimocomun)
# numero1=int(input("Ingrese el primer numero: "))
# numero2=int(input("Ingrese el segundo numero: "))
# mcm(numero1,numero2)

# # 14) Ingresar un quebrado (numerador y denominador) y reducirlo a su mínima expresión.
# def reducir_fraccion(numerador,denominador):
#     for i in range(2,numerador+1):
#         while numerador%i==0 and denominador%i==0:
#             numerador=numerador//i
#             denominador=denominador//i
#     print("Nueva fracción",numerador,"/",denominador)
# numerador=int(input("Ingrese el numerador de la fraccion: "))
# denominador=int(input("Ingrese el denominador de la fraccion: "))
# reducir_fraccion(numerador,denominador)

# 15) Ingresar un número y reportar el número de dígitos que tiene.
# def contar_digitos(numero):
#     cantidad=len(str(numero))
#     print("La cantidad de dígitos es", cantidad)
# numero=int(input("Ingrese el número: "))
# contar_digitos(numero)

# # 16) Ingresar un número y reportarlo al revés
# def numero_invertido(numero):
#     invertido=0
#     while numero !=0:
#         invertido = 10*invertido+numero%10
#         numero= numero//10
#     print("El numero al revés es",invertido)
# numero=int(input("Ingrese el número: "))
# numero_invertido(numero)

# # 17) Ingresar un número y reportar si es capicúa. Un número es capicúa cuando se lee igual 
# # de izquierda a derecha y viceversa. Por ejemplo 2002 es capicúa.
# def numero_invertido(numero):
#     invertido=0
#     while numero !=0:
#         invertido = 10*invertido+numero%10
#         numero= numero//10
#     return invertido
# def capicua():
#     numero = int(input("Ingrese el número a analizar:"))
#     if numero==numero_invertido(numero):
#         print(numero," es capicúa")
#     else: 
#         print(numero,"no es capicúa")
# capicua()
