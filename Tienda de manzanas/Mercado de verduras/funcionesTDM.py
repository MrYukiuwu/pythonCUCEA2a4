def descuentotes(Cantidad,Precio):
    Descuento=0
    if Cantidad >= 10 :
        Descuento = (Cantidad * Precio) * .10
        print(f"El descuento es de {Descuento}")
    #Para un caso especifico,ponlo hasta arriba.
    #Si ocupas mas,todos ponlos arriba del mayor que.

    else :
        print("No hay descuento :c")
        
    return Descuento

def TOTAL(Cantidad,Precio,Descuento):
    
    totalAPagar = (Cantidad * Precio) - Descuento
    print(f"El total es de {totalAPagar}")
    return totalAPagar

import os
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
