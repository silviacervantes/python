import random
'''
class Persona: #Creamos la clase
    piernas=2 #Variable de clase, se accede como Persona.pernas 
    def inicializar(self,nombre): #Constructor
        self.nombre=nombre
    def imprimir(self): #Método para mostrar datos
        print("Nombre: {}".format(self.nombre))
        
        #    El format()método formatea los valores especificados y los inserta dentro del marcador de posición de la cadena.
        #El marcador de posición se define mediante corchetes: {}.
        #El format()método devuelve la cadena formateada.
        

persona1=Persona()
persona2=Persona()
persona1.inicializar("Pedro") #Llamamos al constructor con un nombre
persona1.imprimir() #Mostramos los datos
persona2.inicializar("Carla")
persona2.imprimir()


class Perro:
    # Atributo de Clase, Todos los objetos de esta clase tienen este atributo seteado en "Canis"
    genero= "Canis"
    #Define estado inicial del objeto de esta clase
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad
        
    # Método de instancia
    def imprimir(self):
        return f'{self.nombre} tiene {self.edad} años.'
    
    # Otro método de instancia
    def ladrar(self, sonido):
        return f'{self.nombre} dice {sonido}.'

   
   # Ya que las f-strings son evaluadas al momento de la ejecución tenemos la posibilidad de colocar cualquier expresión válida.
   
#miMascota = Perro()
#otroPerro = Perro()

miMascota = Perro("Popey", 8)
otroPerro = Perro("Bart", 5)

otroPerro.edad= 10
otroPerro.genero= "Felis"

print("Nombre de otroPerro:{} cuya edad es {}".format(otroPerro.nombre,otroPerro.edad))
print(miMascota.imprimir())
print(miMascota.ladrar("Miau"))


############################
#  COLABORACION DE CLASES  #
############################
class Cliente:
    def __init__(self,nombre):
        self.nombre=nombre
        self.monto=0
    def depositar(self,monto):
        self.monto=self.monto+monto
    def extraer(self,monto):
        self.monto=self.monto-monto
    def retornar_monto(self):
        return self.monto
    def imprimir(self):
        print("{} tiene depositada la suma de {}".format(self.nombre,self.monto))
        
class Banco:
    def __init__(self):
        self.cliente1=Cliente("Juan")
        self.cliente2=Cliente("Ana")
        self.cliente3=Cliente("Diego")
    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)
    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
        print("El total de dinero del banco es: {}".format(total))
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

banco1=Banco()
banco1.operar()
banco1.depositos_totales()


class Dado:
    #def __init__(self,valor):
    #    self.valor=valor
    def tirar(self):
        self.valor=random.randint(1,6)
    def imprimir(self):
        print("El valor del dado es{}".format(self.valor))        
    def retornar_valor(self):
        return self.valor

class JuegoDeDados:
    def __init__(self):
        self.dado1=Dado()
        self.dado2=Dado()
        self.dado3=Dado()
    def jugar(self):
        self.dado1.tirar()
        self.dado1.imprimir()
        self.dado2.tirar()
        self.dado2.imprimir()
        self.dado3.tirar()
        self.dado3.imprimir()
        
        if(self.dado1.retornar_valor ==self.dado2.retornar_valor and self.dado1.retornar_valor == self.dado3.retornar_valor ):
            print("GANO")
        else:
            print("PERDIO")
            
juego1 = JuegoDeDados()
juego1.jugar()


########################################################
# COLOCAR UNA CLASE EN UNA COLECCION
########################################################
class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):#forma un string con los datos de la pelicula
        return '{} ({})'.format(self.titulo, self.lanzamiento)


#pelicula1 = Pelicula("Donde estan las rubias","01:56","2004")
#variable = pelicula1.__str__()
#print (variable)


class Catalogo:
    peliculas = [] # Esta lista contendrá objetos de la clase Pelicula
    def __init__(self, peliculas=[]):
        Catalogo.peliculas = peliculas # Hago referencia a una variable de clase!!!!
    def agregar(self, p): # p será un objeto Pelicula
        Catalogo.peliculas.append(p)
    def mostrar(self):
        for p in Catalogo.peliculas:
            print(p) # Print toma por defecto str(p)
        
#Programa principal
pelicula1 = Pelicula("Donde estan las rubias","01:56","2004")
d = Catalogo([pelicula1])
d.mostrar()

p = Pelicula("El Padrino - Parte 1", 175, 1972)
c = Catalogo([p]) # Añado una lista con una película desde el principio
c.mostrar()
c.agregar(Pelicula("El Padrino - Parte 2", 202, 1974)) # Añadimos otra
c.mostrar()
d.mostrar() #Aqui se ve como se modifica la VARIABLE DE CLASE

#GETTER AND SETTER
class ListadoBebidas:
    def __init__(self):
        self.__bebida = 'Naranja'
        self.__bebidas_validas = ['Naranja', 'Manzana']
    @property   #DEFINICION DE GETTER
    def bebida(self):
        return "La bebida oficial es: {}".format(self.__bebida)
    @bebida.setter #DEFINICION DE SETTER
    def bebida(self, bebida):
        self.__bebida = bebida
        
#Programa principal
bebidas= ListadoBebidas()
print(bebidas.bebida)
bebidas.bebida = 'Limonada'
print(bebidas.bebida)

############
# HERENCIA #
############    
class Producto:
    def __init__(self, referencia, nombre,descripcion, precio):
        self.referencia = referencia
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
    
    def __str__(self): #Imprime el objeto
        return "Producto: {} - {} - {} -{}".format(self.referencia,self.nombre,self.descripcion,self.precio)
    
class Adorno(Producto): #Hereda de Producto
    pass
adorno = Adorno(2034, "Vaso adornado", "Vaso de porcelana", 15)
print(adorno)

class Alimento(Producto): #Hereda de Producto
    productor = ""
    distribuidor = ""
    def __str__(self):
        return "Referencia: {} \nNombre: {} \nDescripción: {} \nPrecio: {} \nProductor: {} \nDistribuidor: {}".format(self.referencia, self.nombre, self.descripcion, self.precio, self.productor, self.distribuidor)

class Libro(Producto): #Hereda de Producto
    isbn = ""
    autor = ""
    def __str__(self):
        return "Referencia: {} \nNombre: {} \nDescripción: {} \nPrecio: {} \nISBN: {} \nAutor: {}".format(self.referencia, self.nombre, self.descripcion, self.precio, self.isbn, self.autor)
    
#Programa principal
alimento = Alimento(2035, "Botella de Aceite de Oliva", "250 ML", 5)
alimento.productor = "La Aceitera"
alimento.distribuidor = "Distribuciones SA"
print(alimento,'\n')
libro = Libro(2036, "Cocina Mediterránea","Recetas sanas y buenas", 9)
libro.isbn = "0-123456-78-9"
libro.autor = "Doña Juana"
print(libro,'\n')

class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Vehiculo con color: {} y {} ruedas".format(self.color,self.ruedas)
       
class Auto(Vehiculo):
    def __init__(self,color,ruedas,velocidad):
        #Vehiculo.__init__(self,color, ruedas)
        super().__init__(color, ruedas)
        #De las dos formas esta bien
        self.velocidad = velocidad
    def __str__(self):
        #return "Auto de color {} con {} ruedas y velocidad {}".format(self.color,self.ruedas,self.velocidad)
        return super().__str__()+" y velocidad de"+str(self.velocidad)
        # De las dos formas esta bien

miVehiculo = Vehiculo("Negro",6)
print(miVehiculo)
miAuto = Auto("naranja",4,"50 Km/h")
print(miAuto)

# Programa principal

v1= Vehiculo("Blanco",2)
a1= Auto("Rojo",4,140)
a2= Auto("Negro",4,180)
a3= Auto("Azul",4,200)

print(v1)
print(a1)
print(a2)
print(a3)

vehiculos= []
vehiculos.append(v1)
vehiculos.append(a1)
vehiculos.append(a2)
vehiculos.append(a3)
print(vehiculos[0])
print(vehiculos[2])

class Animal:
    def hablar(self):
        pass
        #return "En animal no tiene definido un habla" 

class Perro(Animal):
    def hablar(self):
        return "GUAU GUAU"
class Gato(Animal):
    def hablar(self):
        return  "MIAU"

for animal in Perro(),Gato():
    print(animal.hablar())
 '''
# Clase abstracta, no puede instanciarse directamente. Se utilizan para construir subclases.
# Evita la duplicacion de codigo

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def mover(self):
        pass
    @abstractmethod
    def emitir_sonido(self):
        print("Animal emite sonido:", end="")

from diapositiva_objetos import Animal #importando desde el archivo
class Gato(Animal):
    def mover(self):
      print("El gato se mueve.")
    def emitir_sonido(self):
        super().emitir_sonido()
        print("Miau!")
        
from diapositiva_objetos import Animal #importando desde el archivo
class Perro(Animal):
    def mover(self):
        print("El perro se está moviendo.")
    def emitir_sonido(self):
        super().emitir_sonido()
        print("Guau, Guau!")

from diapositiva_objetos import Gato
from diapositiva_objetos import Perro
def __main__():
    g1= Gato()
    g1.mover()
    g1.emitir_sonido()
    p1= Perro()
    p1.mover()
    p1.emitir_sonido()
if __name__ == "__main__":
    __main__()
    
#if __name__ == “main”: se usa para ejecutar algún código solo si el archivo se ejecutó directamente y no se importó.