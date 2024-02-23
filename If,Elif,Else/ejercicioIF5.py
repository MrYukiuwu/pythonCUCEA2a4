# Escriba un programa que pida tres números y que escriba si son los tres iguales.
# Si hay dos iguales 
# Si son los tres distintos.
numuno = input("Ingrese el primer numero.  ")
numdos = input("Bien,ahora el segundo.   ")
numtres = input("Excelente,ahora el ultimo numero.   ")

if numuno == numdos == numtres:
    print("Los tres son iguales.")
elif numuno == numdos:
    print("El primero y segundo son iguales.")
elif numdos == numtres:
    print("El segundo y tercer numero son iguales.")
elif numuno == numtres:
    print("El primer y tercer numero son iguales.")
else:
    print("Todos son iguales.")
