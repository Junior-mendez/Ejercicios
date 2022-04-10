# # Ejercicios propuestos de Listas
# 1) Ingresar n números enteros en una lista y mostrar luego, primero la lista de los números 
# pares que fueron ingresados y luego la lista de los números negativos.
cantidad=int(input("Ingrese la cantidad de elementos: "))
lista=[]
listaPares=[]
listaNegativos=[]
for x in range(cantidad):
    numero=int(input("Ingrese el número: "))
    lista.append(numero)
    if (numero%2==0):
        listaPares.append(numero)
    elif(numero<0):
        listaNegativos.append(numero)
print("Lista ingresada:",lista)
print("Lista pares:",listaPares)
print("Lista Negativos:",listaNegativos)


# # 2) Ingresar n enteros en una lista A y otros n enteros en una lista B y mostrar la lista de 
# # enteros del vector C. Donde cada C[i]=A[i]+B[i].

# cantidad=int(input("Ingrese la cantidad de elementos para la lista A y B: "))
# listaA=[]
# listaB=[]
# listaC=[]
# for x in range(cantidad):
#     print("Elemento",x+1,"de la Lista A: ")
#     numeroA=int(input("Ingrese el número: "))
#     listaA.append(numeroA)
#     print("Elemento",x+1,"de la Lista B: ")
#     numeroB=int(input("Ingrese el número: "))
#     listaB.append(numeroB)
#     listaC.append(numeroA+numeroB)
# print("Lista A:",listaA)
# print("Lista B:",listaB)
# print("Lista C:",listaC)

# 3) Calcule la media armónica de un conjunto de datos. La media armónica se define como: el 
# Inverso del promedio de los inversos.

# cantidad=int(input("Ingrese la cantidad de elementos: "))

# suma=0
# for x in range(cantidad):
#     numero=int(input("Ingrese el número: "))
#     suma=suma+1/numero
# print("La media armónica es",cantidad/suma)


# 4) Sea una lista de n elementos reales. Mostrar la lista de números menores al promedio.

# cantidad=int(input("Ingrese la cantidad de elementos: "))
# lista=[]
# listaMenores=[]
# promedio=0
# for x in range(cantidad):
#     numero=int(input("Ingrese el número: "))
#     lista.append(numero)
#     promedio=promedio+numero/cantidad
# for x in range(cantidad):
#     if lista[x]<promedio:
#         listaMenores.append(lista[x])
# print("Lista ingresada:",lista)
# print("Lista menores:",listaMenores)

# 5) Ingresar N notas en una lista y determinar el porcentaje de aprobados y el porcentaje de 
# desaprobados.

# cantidad=int(input("Ingrese la cantidad de notas: "))
# lista=[]
# cantidadAprobados=0
# cantidadDesaprobados=0
# for x in range(cantidad):
#     nota=int(input("Ingrese la nota: "))
#     while nota<0 or nota>20:
#         print("Nota inválida")
#         nota=int(input("Ingrese la nota: "))
#     lista.append(nota)
#     if(nota>=12):
#         cantidadAprobados=cantidadAprobados+1
#     else:
#         cantidadDesaprobados=cantidadDesaprobados+1
# print("Porcentaje Aprobados: ",int((cantidadAprobados*100)/len(lista)),"%")
# print("Porcentaje Desaprobados: ",int((cantidadDesaprobados*100)/len(lista)),"%")

# 6) Ingresar n elementos en una lista y luego ingresar un elemento y reportar cuantas veces 
# aparece ese elemento en la lista

# cantidad=int(input("Ingrese la cantidad de números: "))
# lista=[]
# for x in range(cantidad):
#     numero=int(input("Ingrese el número: "))
#     lista.append(numero)

# numero=int(input("Ingrese el número a buscar: "))
# veces=0
# for x in range(cantidad):
#     if lista[x]==numero:
#         veces=veces+1

# print("El número",numero,"aparece",veces,"veces")


# 7) Ingresar dos listas y reportar si son iguales.

# cantidad1=int(input("Ingrese la cantidad de números para la lista 1: "))
# lista1=[]
# for x in range(cantidad1):
#     numero=int(input("Ingrese el número: "))
#     lista1.append(numero)

# cantidad2=int(input("Ingrese la cantidad de números para la lista 2: "))
# lista2=[]
# for x in range(cantidad2):
#     numero=int(input("Ingrese el número: "))
#     lista2.append(numero)
# if lista1==lista2:
#     print("Las listas son iguales")
# else:
#     print("Las listas no son iguales")


# 8) Calcule la mediana de un conjunto de datos. La mediana de un vector ordenado es el 
# elemento central si el número de términos es impar. Y la semisuma de los términos 
# centrales si el número de términos es par.

# cantidad=int(input("Ingrese la cantidad de números: "))
# mitad=cantidad//2
# lista=[]
# for x in range(cantidad):
#     numero=int(input("Ingrese el número: "))
#     lista.append(numero)
# lista.sort()
# if (cantidad%2==0):
#     mediana=(lista[mitad-1]+lista[mitad])/2
# else:
#     mediana=lista[mitad]
# print("La mediana es",mediana)

# 9) Ingresar 2 listas de n y m elementos y calcular la unión, intersección y la diferencia del 
# primero con el segundo.


# #Primera Forma
# cantidad1=int(input("Ingrese la cantidad de números para la lista 1: "))
# lista1=[]
# for x in range(cantidad1):
#     numero=int(input("Ingrese el número: "))
#     lista1.append(numero)

# cantidad2=int(input("Ingrese la cantidad de números para la lista 2: "))
# lista2=[]
# for x in range(cantidad2):
#     numero=int(input("Ingrese el número: "))
#     lista2.append(numero)
# listaUnion=[]
# listaInter=[]
# listaDifer=[]
# for x in range(cantidad1):
#     for y in range(cantidad2):
#         if(lista1[x]==lista2[y]):
#             listaInter.append(lista1[x])
# listaDifer=list(e for e in lista1 if e not in lista2)
# listaUnion=listaDifer+lista2
# print("Union",listaUnion)
# print("Intercepción",listaInter)
# print("Diferencia de primero a segundo",listaDifer)

# #Segunda Forma
# cantidad1=int(input("Ingrese la cantidad de números para la lista 1: "))
# lista1=[]
# for x in range(cantidad1):
#     numero=int(input("Ingrese el número: "))
#     lista1.append(numero)

# cantidad2=int(input("Ingrese la cantidad de números para la lista 2: "))
# lista2=[]
# for x in range(cantidad2):
#     numero=int(input("Ingrese el número: "))
#     lista2.append(numero)
# primer=set(lista1)
# segundo=set(lista2)

# union= primer | segundo
# intercepcion= primer & segundo
# diferencia= primer - segundo

# print("Union",union)
# print("Intercepción",intercepcion)
# print("Diferencia de primero a segundo",diferencia)


# # Ejercicios de Matrices
# 1. Ingresar una matriz de f filas y c columnas y calcular su matriz transpuesta.
# while True:
#  f=int(input('Numero de filas:'))
#  if f>0:
#     break
# while True:
#  c=int(input('Numero de columnas:'))
#  if c>0:
#     break
# matriz=[]
# matrizResult=[]
# for i in range(f):
#     fila=[]
#     for j in range(c):
#         print('matriz[',i,'][',j,']:',sep='',end='')
#         valor=int(input())
#         fila.append(valor)
#     matriz.append(fila)

# for i in range(c):
#     fila=[]
#     for j in range(f):
#         valor = matriz[j][i]
#         fila.append(valor)
#     matrizResult.append(fila)
# print("La matriz ingresada es",matriz)
# print("La matriz transpuesta es",matrizResult)

# 2. Ingresar una matriz y reportar el mayor elemento de cada fila

# while True:
#  f=int(input('Numero de filas:'))
#  if f>0:
#     break
# while True:
#  c=int(input('Numero de columnas:'))
#  if c>0:
#     break
# matriz=[]
# for i in range(f):
#     fila=[]
#     for j in range(c):
#         print('matriz[',i,'][',j,']:',sep='',end='')
#         valor=int(input())
#         fila.append(valor)
#     matriz.append(fila)
# listaMenores=[]
# for i in range(f):
#     mayor=matriz[i][0]
#     for j in range(c):
#         if(matriz[i][j]>mayor):
#             mayor=matriz[i][j]
#     listaMenores.append(mayor)
# print("Matriz ingresada:",matriz)
# print("Mayor de cada fila:",listaMenores)

# 3. Programa para ingresar una matriz de f filas y c columnas, luego Ingresar un número de
# columna y eliminarla de la matriz.

# while True:
#  f=int(input('Numero de filas:'))
#  if f>0:
#     break
# while True:
#  c=int(input('Numero de columnas:'))
#  if c>0:
#     break
# matriz=[]
# for i in range(f):
#     fila=[]
#     for j in range(c):
#         print('matriz[',i,'][',j,']:',sep='',end='')
#         valor=int(input())
#         fila.append(valor)
#     matriz.append(fila)

# while True:
#     numerocolumna=int(input("Ingrese la columna a eliminar(desde 1):"))
#     if numerocolumna<=c and numerocolumna>0 :
#         break
# columna=[]
# matrizResult=[]
# for i in range(f):
#     fila=[]
#     for j in range(c):
#         if j==numerocolumna-1:
#             columna=matriz[i][j]
#         else:
#             fila.append(matriz[i][j])
#     matrizResult.append(fila)
# print("Matriz ingresada",matriz)
# print("Matriz Resultante",matrizResult)

# 4. Programa para ingresar una matriz de f filas y c columnas , luego ingresar el número de fila 
# e insertar una fila en la matriz.

# while True:
#  f=int(input('Numero de filas:'))
#  if f>0:
#     break
# while True:
#  c=int(input('Numero de columnas:'))
#  if c>0:
#     break
# matriz=[]
# for i in range(f):
#     fila=[]
#     for j in range(c):
#         print('matriz[',i,'][',j,']:',sep='',end='')
#         valor=int(input())
#         fila.append(valor)
#     matriz.append(fila)
# print("Matriz Ingresada",matriz)
# while True:
#     numerofila=int(input("Ingrese la posicion de fila a insertar (desde 1):"))
#     if numerofila<=f and numerofila>0 :
#         filaNueva=[]
#         for x in range(c):
#             numero=int(input("Ingrese el número"))
#             filaNueva.append(numero)
#         break
# matriz.insert(numerofila-1,filaNueva)
# print("Matriz Resultante",matriz)

# 5. Ingresar una matriz de f filas y c columnas y luego intercambiar 2 columnas de la Matriz. El 
# número de las columnas a intercambiar debe ingresarse.

# while True:
#  f=int(input('Numero de filas:'))
#  if f>0:
#     break
# while True:
#  c=int(input('Numero de columnas:'))
#  if c>0:
#     break
# matriz=[]
# for i in range(f):
#     fila=[]
#     for j in range(c):
#         print('matriz[',i,'][',j,']:',sep='',end='')
#         valor=int(input())
#         fila.append(valor)
#     matriz.append(fila)
# print("Matriz Ingresada",matriz)
# while True:
#     c1=int(input("Ingrese el primer numero de columna a intercambiar:"))
#     if c1<=f and c1>0 :
#         break
# while True:
#     c2=int(input("Ingrese el segundo numero de columna a intercambiar:"))
#     if c2<=f and c2>0 :
#         break

# for i in range(f):
#     for j in range(c):
#         cambio=matriz[i][c1-1],matriz[i][c2-1]
#         matriz[i][c2-1],matriz[i][c1-1]=cambio
# print("Matriz Resultante",matriz)

# 6. Programa que ingresa el orden de una Matriz cuadrada y generarla y luego hacer lo
# siguiente:
# a) Calcula la suma de los elementos de la diagonal principal.
# b) Calcula el promedio de los elementos de la diagonal secundaria

# while True:
#  orden=int(input('Numero de orden de matriz cuadrada:'))
#  if orden>0:
#     break
# matriz=[]
# for i in range(orden):
#     fila=[]
#     for j in range(orden):
#         print('matriz[',i,'][',j,']:',sep='',end='')
#         valor=int(input())
#         fila.append(valor)
#     matriz.append(fila)
# print("Matriz Ingresada",matriz)
# principal=0
# secundaria=orden-1
# sumaPrincipal=0
# sumaSecundaria=0
# for i in range(orden):
#     for j in range(orden):
#         if principal==j:
#             sumaPrincipal=sumaPrincipal+matriz[i][j]
#         elif secundaria==j:
#             sumaSecundaria=sumaSecundaria+matriz[i][j]
#     principal=principal+1
#     secundaria=principal-1
# print("Promedio Matriz Principal",sumaPrincipal/orden)
# print("Promedio Matriz Secundaria",sumaSecundaria/orden)

# 7. Ingresar una matriz cuadrada y reportar si es simétrica. Recordar que una matriz es 
# simétrica si se cumple la condición: a[i][j]=a[j][i]

# while True:
#  orden=int(input('Numero de orden de matriz cuadrada:'))
#  if orden>0:
#     break
# matriz=[]
# for i in range(orden):
#     fila=[]
#     for j in range(orden):
#         print('matriz[',i,'][',j,']:',sep='',end='')
#         valor=int(input())
#         fila.append(valor)
#     matriz.append(fila)
# print("Matriz Ingresada",matriz)
# simetrica=True
# for i in range(orden):
#     for j in range(orden):
#         if matriz[i][j] is not matriz[j][i]:
#             simetrica=False
#             break
# if simetrica==True:
#     print("La matriz es simétrica")
# else:
#     print("La matriz no es simétrica")

# 8. Programa para ingresar una matriz de f filas y columnas y luego ordenar las columnas de la 
# matriz.

# while True:
#  f=int(input('Numero de filas:'))
#  if f>0:
#     break
# while True:
#  c=int(input('Numero de columnas:'))
#  if c>0:
#     break
# matriz=[]
# for i in range(f):
#     fila=[]
#     for j in range(c):
#         print('matriz[',i,'][',j,']:',sep='',end='')
#         valor=int(input())
#         fila.append(valor)
#     matriz.append(fila)
# print("Matriz Ingresada",matriz)
# matrizaux=[]
# for j in range(c):
#     columna=[]
#     for i in range(f):
#         columna.append(matriz[i][j])
#         columna.sort()
#     matrizaux.append(columna)
# for i in range(f):
#     fila=[]
#     for j in range(c):
#         valor = matrizaux[j][i]
#         fila.append(valor)
#     matriz[i]=fila
# print("Matriz Resultante",matriz)        
    
    