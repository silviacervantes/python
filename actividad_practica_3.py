'''
1) Crear la clase Persona con los métodos “set_nombre”, “set_edad”,
“get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo
Persona e imprimirlos por consola.

class Persona:
    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_edad(self,edad):
        self.edad=edad
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def print_persona(self):
        print(self.nombre,' ',self.edad)        
    
persona1=Persona()
persona2=Persona()

persona1.set_nombre('Juan Perez')
persona1.set_edad('40')

persona2.set_nombre('Maria Lopez')
persona2.set_edad('38')

persona1.print_persona();
persona2.print_persona();

        

2) Agregarle a la clase anterior un constructor que reciba nombre y edad.


from operator import truediv


class Persona:
    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_edad(self,edad):
        self.edad=edad
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def print_persona(self):
        print(self.nombre,' ',self.edad) 
    def constructor(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def es_mayor_de_edad(self):
        if(self.edad > 18): 
            return True
        else: 
            return False             
    def es_mayor_que(self,peronax):
        if (self.edad > personax.edad):

persona1=Persona()
persona2=Persona()

persona1.constructor('Juan Perez',2)
persona1.print_persona()
print(persona1.es_mayor_de_edad())


3) Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva
True o False.
4) Agregarle un método “es_mayor_que” el cual recibe un objeto persona y
compara su edad con la del objeto actual.
5) Agregarle un método estático “get_mayor” que reciba dos objetos Persona y
devuelva el de edad mayor.
6) Realizar un programa que conste de una clase llamada Alumno que tenga
como atributos el nombre y la nota del alumno. Definir los métodos para
inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la
nota y si ha aprobado o no.´
7) Desarrollar un programa que cargue los datos de un triángulo. Implementar una
clase con los métodos para inicializar los atributos, imprimir el valor del lado
con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o
escaleno).
8) Realizar un programa en el cual se declaren dos valores enteros por teclado
utilizando el método __init__. Calcular después la suma, resta, multiplicación y
división. Utilizar un método para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora.
9) Realizar una clase que administre una agenda. Se debe almacenar para cada
contacto el nombre, el teléfono y el email. Además deberá mostrar un menú
con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto,
Editar contacto, Cerrar agenda.
10) En un banco tienen clientes que pueden hacer depósitos y extracciones de
dinero. El banco requiere también al final del día calcular la cantidad de dinero
que se ha depositado. Se deberán crear dos clases, la clase cliente y la clase
banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos
__init__, depositar, extraer, mostrar_total. La clase banco tendrá como
atributos 3 objetos de la clase cliente y los métodos __init__, operar y
deposito_total.
'''