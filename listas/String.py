nombre = "Pepe"

for letra in nombre :
    print(letra)
#Pone el nombre letra por letra
#p
#e
#p
#e
print(nombre.upper())
#pone todo en mayuscula
#PEPE
print(nombre.lower())
#minuscula
#pepe
print(nombre[0])
#esto con cocrhetes,elige la primera letra del nombre
#p
print(nombre[::-1])
#Esto lo pone al revés
#epeP
print(nombre.replace("e","a"))
#esto reemplaza la e por a
#papa
print(nombre.split("p"))
#parte la letra que indiques
#['Pe', 'e']
print(nombre[0:2])