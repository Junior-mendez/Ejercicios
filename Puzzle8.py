from collections import deque

#Clase que define un nodo en el 8-puzzle.
class Nodo:
    def __init__(self, estado, padre, movimiento, profundidad, piezas_correctas):        
        self.estado = estado                        
        self.padre = padre                          
        self.movimiento = movimiento               
        self.profundidad = profundidad              
        self.piezas_correctas = piezas_correctas    

    def mover(self, direccion):
        estado = list(self.estado)
        ind = estado.index(0)

        if direccion == "arriba":            
            if ind not in [6, 7, 8]:                
                temp = estado[ind + 3]
                estado[ind + 3] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:                
                return None
        elif direccion == "abajo":            
            if ind not in [0, 1, 2]:                
                temp = estado[ind - 3]
                estado[ind - 3] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:                
                return None

        elif direccion == "derecha":            
            if ind not in [0, 3, 6]:                
                temp = estado[ind - 1]
                estado[ind - 1] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:                
                return None
        elif direccion == "izquierda":            
            if ind not in [2, 5, 8]:                
                temp = estado[ind + 1]
                estado[ind + 1] = estado[ind]
                estado[ind] = temp
                return tuple(estado)
            else:                
                return None        

    def encontrar_sucesores(self):
        sucesores = []
        sucesor_arriba = self.mover("arriba")
        sucesor_abajo = self.mover("abajo")
        sucesor_derecha = self.mover("derecha")
        sucesor_izquierda = self.mover("izquierda")
        
        sucesores.append(Nodo(sucesor_arriba, self, "arriba", self.profundidad + 1, calcular_heuristica(sucesor_arriba)))
        sucesores.append(Nodo(sucesor_abajo, self, "abajo", self.profundidad + 1, calcular_heuristica(sucesor_abajo)))
        sucesores.append(Nodo(sucesor_derecha, self, "derecha", self.profundidad + 1, calcular_heuristica(sucesor_derecha)))
        sucesores.append(Nodo(sucesor_izquierda, self, "izquierda", self.profundidad + 1, calcular_heuristica(sucesor_izquierda)))
        
        sucesores = [nodo for nodo in sucesores if nodo.estado != None]  
        return sucesores

    def encontrar_camino(self):
        camino = []
        nodo_actual = self
        while nodo_actual.profundidad >= 1:
            camino.append(nodo_actual)
            nodo_actual = nodo_actual.padre
        camino.reverse()
        return camino
        
    def imprimir_nodo(self):
        renglon = 0
        for pieza in self.estado:
            if pieza == 0:
                print(" ", end = " ")
            else:
                print (pieza, end = " ")
            renglon += 1
            if renglon == 3:
                print()
                renglon = 0       
def calcular_heuristica(estado):
    correcto = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    valor_correcto = 0
    piezas_correctas = 0
    if estado:
        for valor_pieza in estado:
            for valor_correcto in correcto:
                if valor_pieza == valor_correcto:
                    piezas_correctas += 1
                valor_correcto += 1
    return piezas_correctas   

def busqueda(inicial, meta):
    visitados = set()  
    frontera = deque()  
    frontera.append(Nodo(inicial, None, None, 0, calcular_heuristica(inicial)))
    
    while frontera:                         
        nodo = frontera.popleft()          

        if nodo.estado not in visitados:   
            visitados.add(nodo.estado)     
        else:                              
            continue                       
        if nodo.estado == meta:                         
            print("\n¡Se encontró la meta!")            
            return nodo.encontrar_camino()      
        else:                                           
            frontera.extend(nodo.encontrar_sucesores()) 

#Función main.
def main():
    estado_final = (1, 2, 3, 8, 0, 4, 7, 6, 5)
    estado_inicial = (2, 8, 3, 1, 6, 4, 7, 0, 5)

    print("El estado inicial del juego es: ")
    (Nodo(estado_inicial, None, None, 0, calcular_heuristica(estado_inicial))).imprimir_nodo()
    print("\nEscriba (s o S) para iniciar el algoritmo: ")
    print("\tCualquier otra cosa para terminar el programa.")
    algoritmo = input("Su elección: ")
    #Selección de algoritmo
    if algoritmo == "s" or algoritmo == "S":
        print("Corriendo Algoritmo. Por favor espere.")
        nodos_camino = busqueda(estado_inicial, estado_final)
    #Se imprime el camino si existe y si el usuario lo desea.
    if nodos_camino:
        print ("El camino tiene", len(nodos_camino), "movimientos.")
        imprimir_camino = (input ("¿Desea imprimir dicho camino? s/n: "))

        if imprimir_camino == "s" or imprimir_camino == "S":
            print("\nEstado inicial:")
            (Nodo(estado_inicial, None, None, 0, calcular_heuristica(estado_inicial))).imprimir_nodo()
            print ("Piezas correctas:", calcular_heuristica(estado_inicial), "\n")
            input("Presione \"enter\" para continuar.")
            
            for nodo in nodos_camino:
                print("\nSiguiente movimiento:", nodo.movimiento)
                print("Estado actual:")
                nodo.imprimir_nodo()
                print("Piezas correctas:", nodo.piezas_correctas, "\n")     
                input("Presione \"enter\" para continuar.")
    else:
        print ("\nNo se encontró un camino con las condiciones dadas.")
    return 0    
if __name__ == "__main__":
    main()