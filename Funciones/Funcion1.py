nombre="Hugo" #Contexto global
#El contexto global no puede alterar el contexto local.
def saludo(): #Contexto local
    print(nombre)
    print("Buen dia")
#Eso es una funcion,para no repetir lo mismo,solo se ejucta si tu la llamas.
#Podemos usar variables dentro de las funciones.
saludo()    
nombre="Pepe"   
saludo()    
#Por cada vez que lo pongas,se repite.
