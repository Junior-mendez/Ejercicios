def mostrar_divisores(x):
 for i in range(1,x+1):
    if x % i ==0:
        print(i,end=" ")
def esPrimo(x):
 cd=0
 for i in range(1,x+1):
    if x % i ==0:
        cd=cd+1
    if cd==2:
        return True
    else:
        return False