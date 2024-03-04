def descuentotes(Cantidad,Precio):
    if Cantidad == 18:
        Descuento = (Cantidad * Precio) * .15
        print(f"El precio por manzanartes es de {Descuento}")
    #Para un caso especifico,ponlo hasta arriba.
    #Si ocupas mas,todos ponlos arriba del mayor que.
    elif Cantidad >= 10:
        Descuento = (Cantidad * Precio) * .10
        print(f"El descuento es de {Descuento}")


    else :
        print("No hay descuento :c")
        Descuento = 0
    return Descuento

def TOTAL(Cantidad,Precio,descuento):
    
    totalAPagar = (Cantidad * Precio) - Descuento
    print(f"El total es de {totalAPagar}")
    
Descuento = descuentotes(18,15)
TOTAL(18,15,Descuento)
print(Descuento)
Descuento = descuentotes(10,10)
print(Descuento)
Descuento = descuentotes(5,10)
print(Descuento)


food=(input("elige entre Manzanas,Peras,Uvas,Papayas,Sandias,Mango y Maracuya.     "))

print(food)