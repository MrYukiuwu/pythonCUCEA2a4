def descuentotes(Cantidad,Precio):
    if Cantidad == 18:
        Descuento = (Cantidad * Precio) * .15
        print(f"El precio por manzanartes es de {Descuento}")
    #Para un caso especifico,ponlo hasta arriba.
    #Si ocupas mas,todos ponlos arriba del mayor que.
    elif Cantidad >= 10:
        Descuento = (Cantidad * Precio) * .10
        print(f"El descuento es de {Descuento}")
        totalAPagar = (Cantidad * Precio) - Descuento

    else :
        print("No hay descuento :c")
        Descuento = 0
    return Descuento