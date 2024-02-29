def suma(numero1,numero2):
    total= numero1 + numero2
    return total
#El return hace que pueda conservar la variable que quieras,para usarla fuera de la funcion.

def multiplicar(numrero1,numero2):
    total= numrero1 + numero2
    return total

import os
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

#todo lo de arriba es para qu ela funcion de borrar pantalla sirva