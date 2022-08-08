# 1) Crea la clase Vehiculo, extiende la clase y realiza la siguiente implementación:
# Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos. Nota: Puedes utilizar el atributo especial de clase name para recuperar el nombre de la clase de un objeto: type(objeto).__name__

class Vehiculo:
    def __init__(self,color,rueda):
        self.color = color
        self.rueda = rueda
    def __str__(self):
        return "COLOR: {} RUEDAS: {}". format(self.color, self.rueda) 

class Coche(Vehiculo):
    def __init__(self,color,rueda,velocidad,cilindrada):
        super().__init__(color,rueda)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
       return "{} VELOCIDAD: {} CILINDRADA: {}".format(super().__str__(),self.velocidad, self.cilindrada)    

class Bicicleta(Vehiculo):
    tipo = '' #urbana/deportiva
    def __init__(self,color,rueda,tipo):
        super().__init__(color,rueda)
        self.tipo = tipo
    def __str__(self):
       return "{} TIPO: {}".format(super().__str__(),self.tipo)    

class Camioneta(Coche):
    def __init__(self,color,rueda,velocidad,cilindrada,carga):
        super().__init__(color,rueda,velocidad,cilindrada)
        self.carga = carga
    def __str__(self):
       return "{} CARGA: {}".format(super().__str__(),self.carga)    

class Motocicleta(Bicicleta):
    def __init__(self,color,rueda,tipo,velocidad,cilindrada):
        super().__init__(color,rueda,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
       return "{} VELOCIDAD: {} CILINDRADA: {}".format(super().__str__(),self.velocidad, self.cilindrada)    

motocicleta1=Motocicleta('roja','2','URBANA','30Km/h','50cc')
camioneta1=Camioneta('verde','4','120Km/h','2.0cc','1Tonelada')
bicicleta1=Bicicleta('amarilla','2','DEPORTIVA')
coche1=Coche('gris grafito','4','90Km/h','1.0')

vehiculos = []
vehiculos.append(motocicleta1)
vehiculos.append(camioneta1)
vehiculos.append(bicicleta1)
vehiculos.append(coche1)

# 2) Continua con el ejercicio anterior y realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.
'''
def catalogar(vehiculos=[]):
    for v in vehiculos:
        print("TIPO DE VEHICULO: ",type(v).__name__,"Propiedades ==> ",v) 
        # type(objeto).__name__ ==> Muestra el nombre del tipo de objeto
'''
# 3) Continua con el ejercicio anterior y modifica la función catalogar() para que reciba un argumento optativo  ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. También  debe mostrar un mensaje “Se han encontrado {} vehículos con {} ruedas:” únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor
'''
def catalogar(vehiculos=[],ruedas=0):
    suma=0
    for v in vehiculos:
        if(int(v.rueda) == ruedas):
            suma+=1
            print("TIPO DE VEHICULO: ",type(v).__name__,"Propiedades ==> ",v) 
    return ("Se han encontrado {} vehículos con {} ruedas:".format(suma,ruedas))

print(catalogar(vehiculos,4))

print(catalogar(vehiculos,2))

print(catalogar(vehiculos))
'''
# 4) Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee  además explica en un mensaje al usuario la causa y/o solución: resultado = 10/0
'''
try:
    10/0
except:
    print("Division por 0!!!")
else:
    print("No hubo error")
finally:
    print("F I N  de prueba")
'''   

# 5) Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar: Error: Imposible añadir elementos duplicados => [elemento].
 
# Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego muestra su contenido. Sugerencia: podés utilizar la sintaxis “elemento in lista”. elementos = [1, 5, -2]

# Completa el ejercicio aquí

def agregar_una_vez(lista,el):
    if el not in lista:
        lista.append(el)
    else:
        try:
            10/0
        except:
            print("Error: Imposible añadir elementos duplicados => [",el,"].")
        
listado = [1,5,-2]
agregar_una_vez(listado,10)
agregar_una_vez(listado,-2)
agregar_una_vez(listado,"HOLA")
agregar_una_vez(listado,"HOLA")

print(listado)