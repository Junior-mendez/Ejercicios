# # # 1. Se desea calcular independientemente la suma de los pares e impares de los numeros
# # # desde el 1 hasta el 50.

# sumaPar=0
# sumaImpar=0
# for x in range(1,20):
#     if(x%2==0):
#         sumaPar=sumaPar+x
#     else:
#         sumaImpar=sumaImpar+x
# print("La suma de los números pares es",sumaPar )
# print("La suma de los números impares es",sumaImpar )

# # # 2. Calcular el factorial de un número entero mayor o igual que cero.

# numero= int(input("Ingrese un número entero mayor o igual que cero: "))
# factorial=1
# while numero>0:
#     factorial=factorial*numero
#     numero=numero-1
# print("El factorial es",factorial)

# # # 3. Ingresar n números. Se pide calcular el promedio de ellos.

# cantidad= int(input("Ingrese la cantidad de números: "))
# promedio=0
# for x in range(cantidad):
#     numero= int(input("Ingrese el número: "))
#     promedio=promedio+numero/2
# print("El promedio es",promedio)

# # # 4. Sea n un entero positivo. Si n es par, divídalo entre 2, sino lo es, multiplíquelo por 3 y 
# # # súmele 1. Realice este proceso hasta que el número que alcance sea 1. Realice un 
# # # programa en C que implemente dicho proceso. Imprima los números que van 
# # # obteniendo. Por Ejemplo:
# # # Para n = 10 la sucesión generada es: 10 5 16 8 4 2 1

# numero= int(input("Ingrese un número entero positivo: "))
# print("La sucesión generada es:",end=" ")
# while numero!=1:
#     print(numero,end=" ")
#     if(numero%2==0):
#         numero=numero//2
#     else:
#         numero=numero*3+1
# print(numero)

# # # 5. Calcular la sumatoria:
# # #  s= 1 + x + x2/2! + x3/3! + x4/4! + ... + xn/n!
# # # Se debe ingresar x real y n entero positivo

# numero= int(input("Ingrese un número real y entero positivo: "))
# suma=0
# for x in range(1,numero+1):
#     if(x==1):
#         suma=1
#     else:
#         suma=suma+(x*2)//2
# print(suma)