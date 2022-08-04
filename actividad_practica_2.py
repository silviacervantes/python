'''
#Actividad Práctica - Python Unidad 2

# 1) Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.
 
def mayor_de_3(num1, num2,num3):
    mayor = -1
    bandera = True
    if num1 > mayor: 
        mayor=num1

    if(num2 == mayor): 
        bandera = False
    elif num2 > mayor: 
        mayor =num2
        bandera=True

    if num3 == mayor: 
        bandera = False
    elif num3 > mayor: 
        mayor = num3
        bandera=True

    if bandera: 
        return mayor
    else: 
        return -1

val1=int(input("Ingrese un valor > 0: "))
val2=int(input("Ingrese un valor > 0: "))
val3=int(input("Ingrese un valor > 0: "))

mayor = mayor_de_3(val1,val2,val3)

if mayor > 0: print("El mayor de todos es: ", mayor)
else: print("No hay mayor absoluto")




# 2) Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una fecha válida (día, mes, año). Devolver True o False según la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función.

" mes: 01,03,05,07,08,10,12 tienen 31 dias"
" mes: 02 28 dias y 29 bisiesto"
" mes 04 06 09 10 30 dias"
" "


def es_fecha(dia,mes,anio):
    if(anio > 0):
        #Febrero
        if mes == 2 and dia < 29 and dia >0: return True
        elif mes == 2 and dia == 29 and anio%4 ==0: return True
        # Mes con 30 dias
        elif dia >0 and dia < 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 10 ): return True
        elif dia >0 and dia <= 31 and (mes == 1 or mes==3 or mes==5 or mes ==7 or mes == 8 or mes==10 or mes ==12): return True
        else: return False
    else:return False

dia=int(input("DIA:"))
mes=int(input("MES:"))
anio=int(input("AÑO:"))

if es_fecha(dia,mes,anio): print(dia,"/",mes,"/",anio," :Fecha Valida")
else: print(dia,"/",mes,"/",anio," :((!)) Fecha invalida")



# 3) Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero recibido. Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: si la compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1.



def vuelto(imp_compra,imp_recibido):
    if(imp_recibido < imp_compra):return False
    else:
        cambio_500=0
        cambio_200=0
        cambio_100=0
        cambio_50=0
        cambio_20=0
        cambio_10=0

        vuelto_b = imp_recibido-imp_compra
        if(vuelto_b > 500): 
            cambio_500 = vuelto_b//500
            vuelto_b=vuelto_b-(cambio_500*500)
        if(vuelto_b > 200): 
            cambio_200 = vuelto_b//200
            vuelto_b=vuelto_b-(cambio_200*200)
        if(vuelto_b > 100): 
            cambio_100 = vuelto_b//100
            vuelto_b=vuelto_b-(cambio_100*100)
        if(vuelto_b > 50): 
            cambio_50 = vuelto_b//50
            vuelto_b=vuelto_b-(cambio_50*50)
        if(vuelto_b > 20): 
            cambio_20 = vuelto_b//10
            vuelto_b=vuelto_b-(cambio_20*20)
        if(vuelto_b > 10): 
            cambio_10 = vuelto_b//10
            vuelto_b=vuelto_b-(cambio_10*10)
        return(vuelto_b,"------",cambio_500," Billetes de 500",cambio_200," Billetes de 200",cambio_100," Billetes de 100",cambio_50," Billetes de 50",cambio_20," Billetes de 20",cambio_10," Billetes de 10")

importe_total= int(input("Importe total de compra: "))
importe_entregado= int(input("Importe entregado: "))

if not vuelto(importe_total, importe_entregado):
    print("Importe entregado insuficiente") 
else: print(vuelto(importe_total, importe_entregado))




# 4) Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:
def funcion1(cant):
    for i in range(1,cant+1,1):
        print("*"*10)

def funcion2(cant):
    for i in range(2,cant+1,1):
        print("*"*i)

cant_filas = int(input("Ingrese la cantidad de filas:"))
funcion1(cant_filas)
funcion2(cant_filas)


# 5) Crear una función lambda que devuelva el cuadrado de un valor recibido cómo parámetro. Desarrollar además un programa para verificar el comportamiento de la función.
cuadrado = lambda x:x*x
nro = int(input("Ingrese un valor para obtener su cuadrado: ")) 
print(f'El cuadrado de {nro} es:',cuadrado(nro))

# 6) Crear una función lambda para comprobar si un número es par o impar. Desarrollar además un programa para verificar el comportamiento de la función.

es_par = lambda nro:True if nro %2 ==0 else False
numero = int(input("Ingrese un valor para determinar si es par o impar:"))
if es_par(numero):
    print("ES PAR")
else:
    print ("ES IMPAR")

# 7) Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.

cuadrado = lambda x:x*x
n=int(input("Ingrese la cantidad de elementos:"))
lista=[]
for i in range(1,n+1,1):
    lista=lista+[(cuadrado(i))]
longitud = len(lista)
j=0
while j<=10:
    if longitud-1-j > 0:
        print(lista[longitud-1-j])
    j+=1


# 8) Eliminar de una lista de palabras que se encuentren en una segunda lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.
listaA=['rojo','blanco','azul','verde','rosa','violeta','celeste','marron','negro','gris','naranja']
listaB=['verde','naranja','azul','coral']
listaC=[]

print("LISTA ORIGINAL:",listaA)
for i in range(0,len(listaB),1):
    elemento = listaB[i]
    # Cntr+k+c
    if elemento in listaA: 
        listaC.append(listaB[i])
        listaA.remove(listaB[i])
print("PALABRAS A ELIMINAR:",listaC)
print("LISTA RESULTADO:",listaA)
'''
# 9) Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma ascendente o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar además un programa para verificar el comportamiento de la función.
n=int(input("Ingrese cantidad de elementos: "))
lista1 = []
for i in range(0,n,1):
    elemento = input("Elemento:")
    lista1.append(elemento)
lista2=[]
lista2 = sorted(lista1)
print(lista2)
ordenada = lambda resultado: 1 if lista1 == lista2 else 2
if ordenada ==1: print(f"f{lista1} Esta ordenada.") 
else:print(f"{lista1} Esta desordenada.")
'''
# 10) Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita verificar su funcionamiento.
cadena = input("ingrese una cadena para determinar si es capicua:")
def es_palindromo(cadena):
    i=0
    b=True
    while i<= int(len(cadena)/2) and b ==True:
        if(cadena[i] != cadena[len(cadena)-i-1]):
            b=False
        i+=1
    return b

resultado=es_palindromo(cadena)
if(resultado):print(f'{cadena} Es palindromo')
else:print(f'{cadena} NO es palindromo')



# 11) Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas.
cadena = input("Ingrese una cadena de caracters (<80)")
print(cadena.center(80,' '))

# 12) Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada en formato extendido. Por ejemplo, para (12, 10,17) devuelve “12 de Octubre de 2017”. Escribir también un programa para verificar su comportamiento.

tupla = (17,5,81) #empaquetado
def fecha(tupla):
    dia,mes,anio = tupla #desempaquetado
    dia=str(dia)
    mes=str(mes)
    anio=str(anio)
    if mes == '1': mes_name='Enero'
    elif mes == '2': mes_name='Febero'
    elif mes == '3': mes_name='Marzo'
    elif mes == '4': mes_name='Abril'
    elif mes == '5': mes_name='Mayo'
    elif mes == '6': mes_name='Junio'
    elif mes == '7': mes_name='Julio'
    elif mes == '8': mes_name='Agosto'
    elif mes == '9': mes_name='Septiembre'
    elif mes == '10': mes_name='Octubre'
    elif mes == '11': mes_name='Noviembre'
    elif mes == '12': mes_name='Diciembre'
    else: mes_name = 'ERROR'
    anio_name='20'+anio
    return (dia+" de "+mes_name+" de "+anio_name)

print(fecha(tupla))


# 13) Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su longitud.
frase = input("Ingrese una frase:")
palabras= frase.split()
palabras.sort(key=len)
conjunto = set()
for i in range(len(palabras)-1):
    conjunto.add(palabras[i])
print("Contenido de el conjunto:",conjunto)
print("Strin ordenada por longitud de palabras:",palabras)


# 14) Desarrollar una función eliminar_claves() que reciba como parámetros un diccionario y una lista de claves. La función debe eliminar del diccionario todas las claves contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad que indique si la operación fue exitosa. Desarrollar también un programa para verificar su comportamiento.
diccionario={1:'Javier',2:'Cristian',3:'Ruben',4:'George',5:'Daniel',6:'Juan',7:'Juan2',8:'Marcos',9:'Javier2'}
indices = [2,6,3,8,1]
print("Dicccionario completo:",diccionario)

def eliminar_claves(diccionario, l_claves):
    for i in range(len(indices)):
        # print(indices[i])
        diccionario.pop(indices[i])

eliminar_claves(diccionario,indices)
print("Diccionario luego de eliminar los elemenos de los indices:",diccionario)

'''
# 15) Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y cantidad de caracteres dados, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma. Escribir una función utilizando rebanadas

def del_subcadena(cadena,inicio,fin):
    cadena = cadena[0:inicio]+cadena[fin:len(cadena)]
    return cadena

cadena=input("Ingrese una cadena:")
inicio=int(input("Desde que caracter eliminar:"))
fin=int(input("Hasta que caracter eliminar:"))
resultado = del_subcadena(cadena,inicio,fin)
print("La cadena quedo asi:",resultado)

