# ##Ejercicio 1:Escriba un programa para determinar sí un número entero A es divisible por otro B.
# numeroA=int(input("Ingrese el número A: "))
# numeroB=int(input("Ingrese el número B: "))
# if(numeroA%numeroB==0):
#     print(numeroA,"es divisible por",numeroB)
# else:
#     print(numeroA,"no es divisible por",numeroB)

# ###Ejercicio 2: Calcule el interés mensual generado por un capital. La tasa de interés mensual depende del capital 
# # # que fue depositado. Si el capital es menor de 500, la tasa de interés será del 2% mensual. Si el 
# # # capital es mayor o igual que 500 pero menor o igual a 1500 entonces la tasa de interés es de 4.5%. 
# # # Si el capital es mayor que 1500 la tasa de interés es del 9%. Se debe ingresar el capital y reportar 
# # # el interés

# capital=float(input("Ingrese el capital: "))
# if(capital<500):
#     interes=0.02*capital
#     print("El interes mensual es ",interes)
# elif(capital>=500 and capital<=1500):
#     interes=0.045*capital
#     print("El interes mensual es ",interes)
# elif(capital>1500):
#     interes=0.09*capital
#     print("El interes mensual es ",interes)


# ##Ejercicio 3: Diseñe un programa que lea 3 números enteros y determine el número intermedio. No usar operadores lógicos

# num1=int(input("Ingrese el primer numero: "))
# num2=int(input("Ingrese el segundo numero: "))
# num3=int(input("Ingrese el tercer numero: "))

# if(num1>num2):
#     if(num1<num3):
#         print("El numero intermedio es",num1)
#     else:
#          print("El numero intermedio es",num3)
# elif(num2>num1):
#     if(num2<num3):
#         print("El numero intermedio es",num2)
#     else:
#          print("El numero intermedio es",num3)

# ##Ejercicio 4: Escriba un programa que pida una letra minúscula, el programa deberá imprimir si la letra es 
# # una vocal (a, e, i, o, u), semivocal (y) o una consonante.

# letra=input("Ingrese una letra: ")
# if(letra>="a" and letra<="z"):
#     if(letra in ["a","e","i","o","u"]):
#         print("Es una vocal:",letra)
#     elif(letra=="y"):
#         print("Es una semivocal:",letra)
#     else:
#         print("Es una consonante:",letra)
# else:
#      print("No es una letra minúscula:",letra)


# ##Ejercicio 5:Escriba un programa que pida el número de mes (del 1 al 12) y el año e imprima el número de días que tiene el mes.

# mesNumero=int(input("Ingresa el mes en numero: "))
# anio=int(input("Ingresa el año: "))
# if mesNumero in [4, 6, 9, 11]:
#        print("El mes",mesNumero,"tiene 30 días")
# if mesNumero == 2:
#     if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
#         print("El mes",mesNumero,"tiene 29 días")
#     else:
#         print("El mes",mesNumero,"tiene 28 días")
# else:
#     print("El mes",mesNumero,"tiene 31 días")

# ###Ejercicio 6: Un estudiante recibe una propina mensual de S/.100. A fin de mes el estudiante rinde 3 
# # # exámenes (Informática, cálculo, Física). El papa ha decidido incentivarlo dándole una propina 
# # # adicional de 20 soles por cada examen aprobado. Hacer un programa que determine cuanto de 
# # # propina recibe el estudiante después de dar los exámenes.

# notaInformatica=float(input("Ingrese la nota de Informatica:"))
# notaCalculo=float(input("Ingrese la nota de Cálculo:"))
# notaFisica=float(input("Ingrese la nota de Física:"))
# propina=100
# if notaInformatica>11:
#     propina+=20;
# if notaCalculo>11:
#     propina+=20;
# if notaFisica>11:
#     propina+=20;
# print("La propina a recibir es ",propina,"soles")

# ##Ejercicio 7: Calcule el valor de la función Fx, dada por 
# # #  x
# # # 3 + x/2, para x < 0
# # # Fx = 
# # #  4x2 – 2, para x ≥ 0

# valorX=int(input("Ingrese el valor de X: "))
# if valorX>0:
#     resultado=valorX**3+valorX/2
# elif valorX<=0:
#     resultado=4*valorX**2-2

# print("El resultado de la función es",resultado)

# # ###Ejercicio 8: Dados 3 valores enteros X, Y, Z. Elaborar un algoritmo para determinar si esos valores son los 
# # lados de un triángulo.
# # X, Y, Z, son los lados de un triángulo si cumplen con las siguientes condiciones:
# # X>0, Y>0, Z>0, X+Y>Z, X+Z>Y, Y+Z>X
# # Además, clasificar el triángulo por sus lados: Equilátero, Escaleno e Isósceles

# valorX = int(input("Ingrese el valor de X: "))
# valorY = int(input("Ingrese el valor de Y: "))
# valorZ = int(input("Ingrese el valor de Z: "))

# if valorX<(valorY+valorZ) and valorY<(valorX+valorZ) and valorZ<(valorX+valorY):
#   print('Si a =',valorX,', b =',valorY,'y c =',valorZ,' entonces si se puede hacer un triangulo')
#   if valorX==valorY==valorZ:
#     print('Equilatero')
#   elif valorX==valorY or valorY==valorZ or valorX==valorZ:
#     print('Isósceles')
#   else:
#     print('Escaleno')
# else:
#   print('Si a =',valorX,', b =',valorY,'y c =',valorZ,' entonces no se puede hacer un triangulo')

# #Ejercicio 9: Ingresar un número entero de 4 dígitos y determinar si todos los dígitos del número son pares. 
# # Por ejemplo, si el número es: 7286 no cumple la condición ya que el digito 7 es impar, por el 
# # contrario, el numero 8424 si cumple la condición pues todos los dígitos son pares.

# numero = int(input("Ingrese el numero a analizar: "))
# while numero>0:
#     digito=numero%10
#     numero= int(numero/10)
#     if(digito%2==0):
#         print("El número ",digito,"es par")
#     else:
#         print("El número ",digito,"es impar")


# # # Ejercicio 10: En el curso de Algoritmos se rinden 4 exámenes de las cuales se elimina la menor nota. Hacer 
# # # un programa para ingresar las notas de los 4 exámenes y reportar la nota eliminada y el 
# # # promedio final del alumno

# notas=[]
# for x in range(4):
#     nota=int(input("Ingrese la nota: "))
#     while(nota<0 or nota>20):
#         print("¡Nota Inválida!!")
#         nota=int(input("Ingrese la nota: "))
#     notavalida=nota
#     notas.append(notavalida)
# print("Notas ingresadas",notas)
# notas.sort()
# print("Notas Ordenadas",notas)
# notamenor=notas[0]
# print("Nota menor",notamenor)
# notas.pop(0)
# print("Notas Finales",notas)
# promedio=0
# for x in range(len(notas)):
#     promedio=promedio+notas[x]
# print("Promedio",promedio/len(notas))

# # #Ejercicio 11: Una empresa paga a sus vendedores un sueldo igual al 10% del monto total vendido más S/. 25 
# # # por cada S/.500 de venta en exceso sobre S/. 5000. Diseñe un programa que permita calcular 
# # # el sueldo de un vendedor.
# totalVendido=float(input("Ingrese el total vendido: "))
# if(totalVendido>5000):
#     sueldo=0.10 * totalVendido + 0.25 * (totalVendido/500)
# else:
#     sueldo=0.10*totalVendido
# print("El sueldo del vendedor es",sueldo)

# # # Ejercicio 12: Dado un número natural de tres cifras, diseñe un algoritmo que determine si el número es o no 
# # # capicúa. Un número es capicúa si se lee igual de derecha a izquierda que de izquierda a derecha. 
# # # Así, por ejemplo, 363 es capicúa; pero, 356 no lo es.

# numero=int(input("Ingrese un número de 3 dígitos: "))
# a=int(numero/100)
# b=numero%10
# if(a==b):
#     print("El número",numero,"es capicúa")
# else:
#     print("El número",numero,"no es capicúa")

# # Ejercicio 13: El índice de masa corporal (IMC) permite medir el grado de sobrepeso u obesidad de una 
# # persona. El IMC de una persona se calcula con la fórmula:
# # IMC = peso/estatura2
# # Estando el peso en kilogramos y la estatura en metros. En base al valor del IMC, se obtiene el 
# # # grado de obesidad de la persona de acuerdo a la tabla adjunta.

# # peso=float(input("Ingrese su peso en kilogramos: "))
# # estatura=float(input("Ingrese su estatura en metros: "))
# # imc=peso/estatura**2
# # if(imc<20):
# #     print("Delgado")
# # elif(imc>=20 and imc<25):
# #     print("Normal")
# # elif(imc>=25 and imc<27):
# #     print("Sobrepeso")
# # elif(imc>=27):
# #     print("Obesidad")
