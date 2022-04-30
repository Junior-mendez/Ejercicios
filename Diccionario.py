# # Ejercicio 1
# # Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean
# # desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.
# def diccionario(n):
#     numeros={}
#     for i in range(1,n+1):
#         numeros[i]=i**2
#     print("Diccionario:",numeros)
# while True:
#     numero=int(input("Ingrese un número mayor a cero:"))
#     if numero>0:
#         break
# diccionario(numero)

# # Ejercicio 2
# # Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada 
# # carácter en la cadena.
# def contar_caracter(cadena):
#     apariciones={}
#     for i in cadena:
#         if i in cadena:
#             cantidad=cadena.count(i)
#             apariciones[i]=cantidad
#     print("Diccionario apariciones",apariciones)
# cadena=input("Ingrese la expresión o cadena:")
# contar_caracter(cadena)


# # Ejercicio 3
# # Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de 
# # las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos 
# # mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe 
# # nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
# frutas={"manzana":3,"mango":1,"platano":2}
# def calcular_monto(nombre,cantidad):
#     resultado=0
#     for key,valor in frutas.items():
#         if key==nombre:
#             resultado=valor*cantidad
#             print("El monto",resultado)
#     if resultado==0:
#         print("La fruta ingresada no se encuentra")
# while True:
#     fruta=input("Ingrese la fruta:")
#     cantidad=input("Ingrese la cantidad vendida:")
#     calcular_monto(fruta,cantidad)
#     opcion=input("Ingrese la letra 'S' si desea realizar otra consulta:")
#     if opcion != "S" and opcion != "s":
#         break

# # Ejercicio 4
# # Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las 
# # notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en 
# # un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de 
# # cada alumno.
# # El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus 
# # notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos 
# # y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya 
# # existe el programa nos dará un error.
# notas_alumno={}
# def registrar_notas(alumno,notas):
#     if alumno in notas_alumno:
#         print("El alumno ya se encuentra registrado")
#     else:
#         notas_alumno[alumno]=notas
# def alumno(cantidad):
#     for i in range(cantidad):
#         nombre=input("Ingrese el nombre del alumno:")
#         notas=[]
#         while True:
#             nota=int(input("Ingrese la nota a registrar: "))
#             if(nota<0):
#                 break
#             notas.append(nota)
#         registrar_notas(nombre,notas) 
# def calcular_promedio(notasalumno):
#     for key,value in notasalumno.items():
#         promedio=0
#         for i in value:
#             promedio=promedio+i/2
#         print("Alumno:",key,"Promedio:",promedio)
# cantidad=int(input("Ingrese el número de alumnos a registrar: "))
# alumno(cantidad)
# print("Diccionario de notas:",notas_alumno)
# calcular_promedio(notas_alumno)

# # Ejercicio 5
# # Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números 
# # de teléfono. El programa nos dará el siguiente menú:
# # Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono 
# # y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir 
# # ingresar el teléfono correspondiente.
# # Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen 
# # por dicha cadena.
# # Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# # Listar: Nos muestra todos los contactos de la agenda.
# # Implementar el programa con un diccionario
agenda={}
def anadir_modificar(nombre):
    if nombre in agenda:
        numero=int(input("Ingrese el numero nuevo del contacto: "))
        for key in agenda:
            if nombre==key:
                agenda[key]=numero
            print("Contacto modificado:",nombre,"-> Número:",numero)
    else:
        numero=int(input("Ingrese el numero del contacto: "))
        agenda[nombre]=numero
    print("Contacto agregado:",nombre,"-> Número:",numero)
def buscar(cadena):
    for key,value in agenda.items():
        if cadena in key:
            print(key,":",value)
def borrar(nombre):
    if nombre in agenda:
        confirmacion=input("Está seguro que desea eliminar el contacto escriba 'S' para confirmar: ")
        if confirmacion=='S' or confirmacion=='s':
            del agenda[nombre]            
def menu():
    while True:
        print("########### AGENDA ##############")
        print("1. Añadir/Modificar contacto")
        print("2. Buscar contacto")
        print("3. Borrar contacto")
        print("4. Listar contacto")
        print("5. Salir")
        opcion=int(input("Ingrese la opción:"))
        if opcion==1:            
            nombre=input("\nIngrese el nombre a añadir o modificar: ")
            anadir_modificar(nombre)
        elif opcion==2:
            print("########### BÚSQUEDA DE CONTACTO ############")
            nombre=input("\nIngrese el nombre a buscar: ")
            buscar(nombre)
        elif opcion==3:
            print("########### ELIMINAR CONTACTO ############")
            nombre=input("\nIngrese el nombre a borrar: ")
            borrar(nombre)
        elif opcion==4:
            print("########### LISTADO DE CONTACTOS ############")
            print(agenda)
        if opcion==5:
            break
menu()



