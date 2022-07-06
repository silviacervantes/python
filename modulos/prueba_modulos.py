#Importo toda la libreria del modulo saludar
import saludar
saludar.saludos()

#Importo solo la funcion saludos
from saludar import saludos
saludos()

#Importo TODAS LAS FUNCIONES
from saludar import *
saludos()
#Importar clases
from saludar import Saludo
s = Saludo()

