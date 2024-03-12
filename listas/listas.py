# numero = "694200,6969696969,8764574657,69"
# ListaDeNumeros=[694200,6969696969,8764574657,69]
# #print(numero.split(","))
# #for numero in numero.split(","):
# #    print(numero)
# print(numero[0])
# #6
# print(ListaDeNumeros[0])
# #agarra el primer grupo
# #694200
# print(len(ListaDeNumeros))
# #esto te cie cuantos numeros hay en tu lista
# #5

calificacionTaller = []
contador = 0
while contador <13:
    calificacion= float(input("Ingreasa la primera calificacion:  "))
    calificacionTaller.append(calificacion)
    #esto guarda todos los datos para la lista
    contador+=1
print(calificacion)
suma=0
for calificacion in calificacionTaller:
    suma = suma + calificacion
    promedio = suma / len(calificacionTaller)
print(promedio)