test_list = [1, 4, 5, 8, 10] 
  
print ("Original list : " + str(test_list)) 
  
flag = 0
if(test_list == sorted(test_list)): 
    flag = 1
      
if (flag) : 
    print ("Yes, List is sorted.") 
else : 
    print ("No, List is not sorted.") 
    

'''
Prueba inicial
'''

def suma_numeros(numeros): # Bloque 1
    suma = 0 # Bloque 2
    for n in numeros: # Bloque 2
        suma += n # Bloque 3
        print(suma) # Bloque 3
    return suma # Bloque 2


print("Suma de numeros",suma_numeros([3,4]))

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


frutas = ["manzana", "plátano", "cereza", "naranja", "kiwi", "melón", "mango"]
print(frutas[2:5])