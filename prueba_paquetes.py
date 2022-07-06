# Accediendo al paquete modulos
 
#Importo solo la funcion saludos
from modulos.saludar import saludos
saludos()

#Importo TODAS LAS FUNCIONES
from modulos.saludar import *
saludos()

#Importar clases
from modulos.saludar import Saludo
s = Saludo()

