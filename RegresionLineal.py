# a. Sean x los gastos de publicidad y y las ventas. Utilice el método de mínimos cuadrados 
# para desarrollar una aproximación de línea recta de la relación entre las variables.
# b. Utilice la ecuación desarrollada en el inciso a para pronosticar las ventas para un gasto 
# de publicidad de $8 000

import math


x=[1,4,6,10,14]
y=[19,44,40,52,53]

sx,sy,sxy,sxx=0,0,0,0
n=len(x)
for i in range(n):
    print(x[i],y[i])

for i in range(n):
    sx=sx+x[i]
    sy=sy+y[i]
    sxy= sxy + x[i] * y[i]
    sxx= sxx + x[i] * x[i]
b1 = (sxy-(sx*sy)/n)/(sxx - math.pow(sx,2)/n)
b0 = sy/n - b1*(sx/n)

if b1>0:
    print('y=',b0,"+",b1,"x")
else:
    print('y=',b0,b1,"x")

numEst=int(input("Gasto de publicidad (en miles):"))
ventas=b0+b1*numEst
print("Las ventas serian",ventas,"mil dolares")