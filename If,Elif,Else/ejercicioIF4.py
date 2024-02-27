print("Bienvendiso al calculador de años biciestos 3000")
year = int(input ("ingrese un año."))
#Debe ser divisible por 4,no por 100,solo si es 400
if year % 4 !=0:
    #El % e una division,que te da el residuo.
    print("No es")
elif year % 4 == 0 and year % 100 !=0:
    print("sies")
elif year % 4 == 0 and year % 100 ==0: and year % 400 !=0:
    print("noes")
elif year % 4 == 0 and year % 100 ==0: and year % 400 ==0:
    print("Sies")
#incompleto