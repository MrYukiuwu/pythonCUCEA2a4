multiplicador = float (input("ingresa el numero al cual quieres ver sus multiplicaciones de 0 al 100.   "))
multiplicando = 0
while multiplicando <= 100:
    print (f"{multiplicador} x {multiplicando} = {multiplicador * multiplicando}")
    multiplicando += 1
    #esto significa multiplicando = multiplicando + 1