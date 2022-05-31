'''
Prueba inicial
'''
print("Hola mundo");
for i in range (20,0,-1):
    print (i)

''' 
Declaracion de variables
'''
cadena="hola mundo"
entero = 3
flotante = 17.5
logico = False 

'''
Salida pantalla con varios datos
'''
print("Cadena:",cadena, "Entero:",entero, "Flotante:",flotante,\
    "Logico:", logico)

'''
Ingreso de datos por pantalla y calculo integrado en la salida
'''
lado = 3
#lado=int(input("Ingrese el lado del cuadrado: "))

print("La superficie del cuadrado es:",lado*lado) 
print("El perimetro del cuadrado es: ",lado*4)

#OTRO TIPO DE COMENTARIO3

'''
Obtener el tipo de datos de las variables definiddas anteriormente
'''
print(type(flotante))

'''
ejemplo de bloque - x identacion - y estructuras de control
'''
nombre = input("Ingrese un nombre: ")
print(nombre[0]) #se imprime la primer letra
if nombre[0]=="J": #verificamos si el primer caracter del string es una j
    print(nombre)
    print("comienza con la letra J")

