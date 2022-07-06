'''
#Manejo de Excepciones
while (True): #Itera hasta que ingrese el valor valido
    try:
        n = float(input("Ingrese un número: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("ERROR, Ingrese un numero !!! ") # Maneja la excepcion
    else:
        print("SIN ERRORES") # Si no hay exepciones sale del bucle
        break
    finally:
        print("FIN DE EJECUCION") # Se ejecuta siempre haya o no excepciones

      
#Ejemplo con main()   
def funcion(x,y):
    return x/y
def main():
    x = float(input('x: '))
    y = float(input('y: '))
    #return f'El resultado de {x}/{y} es {funcion(x,y)}'
    print(funcion(x,y))
main()
 
#Multiples Excepciones
try:
    n = input("Ingrese un número: ") # No transformamos a número
    5/n
except Exception as e: # Guardamos la excepción como una variable e
    print("Ha ocurrido un error =>", type(e).__name__) #Muestra el nombre del tipo de excepcion
'''     
try:
    n = float(input("Ingrese un número divisor: "))
    5/n
except TypeError:
    print("No se puede dividir el número entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")
except Exception as e: #Engloba cuakquier tipo de error
    print("Ha ocurrido un error no previsto", type(e).__name__)
    

