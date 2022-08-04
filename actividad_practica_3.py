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


class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Persona nombre: {} - Persona Edad: {}".format(self.nombre,self.edad)
    
persona1 = Persona("Silvia","41")
print(persona1.__str__())




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


class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Persona nombre: {} - Persona Edad: {}".format(self.nombre,self.edad)
    
    def es_mayor_de_edad(self):
        if int(self.edad) > 18:
            return True
        else: 
            return False
        
    
persona1 = Persona("Silvia","41")
print(persona1.__str__())
if(persona1.es_mayor_de_edad()):
    print ("Es MAYOR de edad")
else: 
    print("Es   m e n o r    de edad")



4) Agregarle un método “es_mayor_que” el cual recibe un objeto persona y
compara su edad con la del objeto actual.



class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Persona nombre: {} - Persona Edad: {}".format(self.nombre,self.edad)
    
    def es_mayor_de_edad(self):
        if int(self.edad) > 18:
            return True
        else: 
            return False
    
    def es_mayor_que(self, persona2):
        if int(self.edad) > int(persona2.edad):
            return True
        else:
            return False
    
    
persona1 = Persona("Silvia","41")
persona2 = Persona("Aldo","32")

if (persona1.es_mayor_que(persona2)):
    print("{} es mayor que {}".format(persona1.nombre, persona2.nombre))
else: 
    print("{} es mayor que {}".format(persona2.nombre, persona1.nombre))
    


5) Agregarle un método estático “get_mayor” que reciba dos objetos Persona y
devuelva el de edad mayor.

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Persona nombre: {} - Persona Edad: {}".format(self.nombre,self.edad)
    
    def es_mayor_de_edad(self):
        if int(self.edad) > 18:
            return True
        else: 
            return False
    
    def es_mayor_que(self, persona2):
        if int(self.edad) > int(persona2.edad):
            return True
        else:
            return False
    
    def get_mayor(self, persona2):
        if(self.es_mayor_que(persona2)):
            return self
        else: 
            return persona2
        
        
    
persona1 = Persona("Silvia","41")
persona2 = Persona("Aldo","32")

mayor=persona1.get_mayor(persona2)
print("MAYOR==>",mayor.__str__())


6) Realizar un programa que conste de una clase llamada Alumno que tenga
como atributos el nombre y la nota del alumno. Definir los métodos para
inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la
nota y si ha aprobado o no.´

class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        return "Alumno: {}, Nota: {}".format(self.nombre,self.nota)
    
    def aprobado(self):
        if(int(self.nota) >= 6): 
            return "Aprobado"
        else:
            return "Desaprobado"

alumno1 = Alumno("Carolina","7")
print(alumno1.__str__()," - ",alumno1.aprobado())




7) Desarrollar un programa que cargue los datos de un triángulo. Implementar una
clase con los métodos para inicializar los atributos, imprimir el valor del lado
con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o
escaleno).

class Triangulo:
    def __init__(self,lado1,lado2,lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
    def tipo(self):
        lado1=int(self.lado1)
        lado2=int(self.lado2)
        lado3=int(self.lado3)
        
        if(lado1 == lado2 and lado1 == lado3):
            return "EQUILATERO"
        elif (lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
            return "ESCALENO"
        else: return "ISOCELES"
    
    def lado_mayor(self):
        lado1=int(self.lado1)
        lado2=int(self.lado2)
        lado3=int(self.lado3)
        
        mayor = lado1
        if lado2 > mayor:
            mayor = lado2
        elif lado3 > mayor:
            mayor = lado3
        return mayor
    
triangulo1 = Triangulo("10","3","13")    

print("El mayor lado del triangulo mide:",triangulo1.lado_mayor()," y es del tipo:",triangulo1.tipo())        


8) Realizar un programa en el cual se declaren dos valores enteros por teclado
utilizando el método __init__. Calcular después la suma, resta, multiplicación y
división. Utilizar un método para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora.

class Calculadora:
    def __init__(self,valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    def suma(self):
        valor1 = self.valor1
        valor2 = self.valor2
        return "El valor de la suma es {}".format(valor1+valor2)
    def resta(self):
        valor1 = self.valor1
        valor2 = self.valor2
        return "El valor de la resta es {}".format(valor1-valor2)
    def multiplicacion(self):
        valor1 = self.valor1
        valor2 = self.valor2
        return "El valor de la Multiplicacion es {}".format(valor1*valor2)
    def division(self):
        valor1 = self.valor1
        valor2 = self.valor2
        return "El valor de la division es {}".format(valor1/valor2)

numero1 = float(input("Ingrese un numero para la calculadora: "))
numero2 = float(input("Ingrese otro numero para la calculadora: "))

calculadora1 = Calculadora(numero1,numero2)

print (calculadora1.suma())
print (calculadora1.resta())
print (calculadora1.multiplicacion())
print (calculadora1.division())



9) Realizar una clase que administre una agenda. Se debe almacenar para cada
contacto el nombre, el teléfono y el email. Además deberá mostrar un menú
con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto,
Editar contacto, Cerrar agenda.

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def __str__(self):
        return "Nombre:{} - Telefono:{} - Email:{}".format(self.nombre, self.telefono, self.email)
   
    def editar_nombre(self,nombre):
        self.nombre = nombre
        
    def editar_telefono(self,telefono):
        self.telefono = telefono

    def editar_email(self,email):
        self.email = email
        

class Agenda:
    contactos = []
    def __init__(self,contactos=[]):
        self.contactos = contactos
    
    def agregar(self,contacto):
        self.contactos.append(contacto)    
    
    def editar(self,contacto,parametro,valor):
        contacto_a_editar=self.buscar(contacto)
        if(parametro == 'nombre'):
            contacto_a_editar.editar_nombre(valor)
        if(parametro == 'telefono'):
            contacto_a_editar.editar_telefono(valor)
        if(parametro == 'email'):
            contacto_a_editar.editar_email(valor)
    
    def listar(self):
        for c in self.contactos:
            print(c)        
    
    def buscar(self,contacto):
        for c in self.contactos:
            if(c == contacto):
                return c
    
    def cerrar(self):
        pass  
      

c1=Contacto("Silvia","4282397","silviaccp@gmail.com")
c2=Contacto("Verena","3876157201","verena@gmail.com")

agenda1 = Agenda()
agenda1.agregar(c1)
agenda1.agregar(c2)
agenda1.editar(c1,"telefono","123")
print(agenda1.listar())
print(agenda1.buscar(c2))



10) En un banco tienen clientes que pueden hacer depósitos y extracciones de
dinero. El banco requiere también al final del día calcular la cantidad de dinero
que se ha depositado. Se deberán crear dos clases, la clase cliente y la clase
banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos
__init__, depositar, extraer, mostrar_total. La clase banco tendrá como
atributos 3 objetos de la clase cliente y los métodos __init__, operar y
deposito_total.
'''
class Cliente:
    def __init__(self,nombre,cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    def depositar(self,cantidad):
        self.cantidad = int(self.cantidad)+cantidad
    def extraer(self,cantidad):
        if(int(self.cantidad) > cantidad):
            self.cantidad = int(self.cantidad)-cantidad
    def mostrar_total(self):
        return self.cantidad
    def __str__(self):
        return "Nombre:{} - Cantidad:{}".format(self.nombre, self.cantidad) 

class Banco:
    c1=''
    c2=''
    c3=''
    def __init__(self):
        self.c1 = Cliente("Silvia","1000")
        self.c2 = Cliente("Verena","2500")
        self.c3 = Cliente("Gladys","100000")
    def operar(self):
        self.c1.depositar(300)
        self.c2.extraer(20)
    def deposito_total(self):
        print("Deposito Total:",int(self.c1.mostrar_total())+int(self.c2.mostrar_total())+int(self.c3.mostrar_total()))
    def __str__(self):
        return "{}/n {}/n {}".format(self.c1,self.c2,self.c3)
    
            
banco1 = Banco()
banco1.deposito_total()
banco1.operar()
banco1.deposito_total()
print(banco1)

    
        