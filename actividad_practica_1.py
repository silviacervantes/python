# 1)Escribe un programa muestre por pantalla “Hello World”.
from ast import Break
from inspect import isclass


print("Hola Mundo")

# 2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.
resultado = 3+5
print("El resultado de 3+5 es:",resultado)

#3) Escribe un programa que pida el nombre del usuario y escriba un texto que diga “Hola nombreUsuario”
nombreUsuario=input("Ingrese nombre de usuario: ")
print("Hola ",nombreUsuario)

# 4) Escribe un programa que pida un número, pida otro número y escriba el resultado de sumar estos dos números.
numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))
print("El resuldao de sumar ",numero1," con ",numero2, " es :",numero1+numero2)

# 5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))
if(numero1 > numero2):
    print("El mayor es ", numero1)
else:
    print("El mayor es ", numero2)

# 6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.
numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))
numero3 = float(input("Ingrese otro numero: "))
mayor = 0
if(numero1 > numero2):
    mayor = numero1
else:
    mayor = numero2
if (numero3 > mayor):
    mayor = numero3

print("El mayor es: ",mayor)

# 7) Escribe un programa que pida un número y diga si es divisible por 2
numero = float(input("Ingrese un numero (/2): "))
resto = numero%2
if resto ==0:
    print("El numero es divisible por 2.")
else:
    print("El numero no es divisible por 2")


#8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)
#CASE?

numero = float(input("Ingrese un numero para verificar si es divisible por 2,3,5 o 7): "))
if (numero%2 ==0):
    print("El numero es divisible por 2.")
    Break
elif(numero%3 ==0 ):
    print("El numero no es divisible por 3.")
    Break
elif(numero%5==0):
    print("El numero es divisible por 5.")
    Break
elif(numero%7==0):
    print("El numero es divisibl por 7.")
    Break
else:
    print("El numero no es divisible por 2 3 5 ni 7")

 

# 9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay que decir todos por los que es divisible)

numero = float(input("Ingrese un numero para verificar si es divisible por 2,3,5 o 7): "))
if (numero%2 ==0):
    print("El numero es divisible por 2.")
if(numero%3 ==0 ):
    print("El numero no es divisible por 3.")
if(numero%5==0):
    print("El numero es divisible por 5.")
if(numero%7==0):
    print("El numero es divisibl por 7.")



# 10) Escribir un programa que escriba en pantalla los divisores de un número dado
numero = int(input("Ingrese un numero para visualizar los divisores del mismo: "))
for i in range(2,(int((numero)/2)+1),1):
    if(numero%i==0):
        print("Divisible por: ",i)
    


# 11) Escribir un programa que nos diga si un número dado es primo (no es divisible por ninguno otro número que no sea él mismo o la unidad)

numero = int(input("Ingrese un numero para visualizar los divisores del mismo: "))
b = False 
for i in range(2,(int((numero)/2)+1),1):
    if(numero%i==0):
        #print(i)
        b = True
if b == False: 
    print(numero," Es Primo")
else:
    print(numero," No es primo")


# 12) Pide una nota (número). Muestra la calificación según la nota:
#  0-3: Muy deficiente
#  3-5: Insuficiente
#  5-6: Suficiente
#  6-7: Bien
#  7-9: Notable
#  9-10: Sobresaliente

nota = int(input("Ingrese una nota (0-10):"))
if nota <= 3 and nota >= 0: print(nota,":Muy deficiente")
elif nota <= 5 : print(nota,":Insuficiente")
elif nota <= 6 : print(nota,":Suficiente")
elif nota <= 7 : print(nota,":Bien")
elif nota <= 9 : print(nota,":Notable")
elif nota <= 10 : print(nota,":Sobresaliente")


# 13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente forma:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# ……….

for i in range(0,31,1):
    fila=''
    for j in range(0,i,1):
        fila = fila + str(i)
    print(fila)



# 14) Haz un programa que escriba una pirámide inversa de los números del 1 al número que indique el usuario de la siguiente forma (suponiendo que indica 6):
# 666666
# 55555
# 4444
# 333
# 22
# 1


for i in range(6,0,-1):
    fila=''
    for j in range(0,i,1):
        fila = fila + str(i)
    print(fila)




'''
15) Crear un programa que escriba los números del 1 al 500, y que indique cuales son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal. Por ejemplo:
1
2
3
4 (Múltiplo de 4)
5
------------------------------------------------------------
6
7
8 (Múltiplo de 4)
9 (Múltiplo de 9)
10
'''
for i in range(1,501,1):
    if i%4 ==0 and i%9==0: print(i," (Multiplo de 4 y 9)")
    elif i%4 ==0: print(i," (Multiplo de 4)")
    elif i%9 == 0: print(i," (Multiplo de 9)")
    else:print(i)
    if i%5 ==0: print("------------------------------------------------------------")