import funcionesTDM
import os

food=(input("elige entre Manzanas,Peras,Uvas,Papayas,Sandias,Mango y Maracuya.     "))
Descuento = 0
funcionesTDM.borrarPantalla()

Cantidad= float (input(f"Ingresa cuanto de {food} quieres vender. "))

while Cantidad != 0:

    
    Precio= float (input(f"Ingresa el precio de {food}. "))

    funcionesTDM.borrarPantalla()
    Descuento=funcionesTDM.descuentotes(Cantidad,Precio)
    funcionesTDM.TOTAL(Cantidad,Precio,Descuento)
    
    Cantidad=(input(f"Ingresa cuanto de {food} quieres vender. "))
    if Cantidad==0:
        break
#Le falta :(
    
    
    #Termina con la preguinta para ver si quieres romper el ciclo.
    #Hay ota version,en donde usas if y break.
print("Gracias por comprar,tqm.")