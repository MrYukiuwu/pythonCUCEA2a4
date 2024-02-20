Descuento = 0
CantidadDeManzanas= float (input("Ingresa cuantas manzanas quieres vender. "))
PrecioDeLasManzanas= float (input("Ingresa el precio de las manzanas. "))

totalAPagar = CantidadDeManzanas * PrecioDeLasManzanas
if CantidadDeManzanas == 18:
    Descuento = (CantidadDeManzanas * PrecioDeLasManzanas) * .15
    print(f"El precio por manzanartes es de {Descuento}")
#Para un caso especifico,ponlo hasta arriba.
#Si ocupas mas,todos ponlos arriba del mayor que.
elif CantidadDeManzanas >= 10:
    Descuento = (CantidadDeManzanas * PrecioDeLasManzanas) * .10
    print(f"El descuento es de {Descuento}")
    totalAPagar = (CantidadDeManzanas * PrecioDeLasManzanas) - Descuento
    print(f"El total es {totalAPagar}")

else :
    print("No hay descuento :c")
    print(f"El total es {totalAPagar}")
print("Gracias por comprar,tqm.")