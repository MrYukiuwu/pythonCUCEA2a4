nombre="Hugo" #Contexto global
#El contexto global no puede alterar el contexto local.
def saludo(): #Contexto local
    nombre = "Yuki"
    print(nombre)
    print("Buen dia")
#Solo cambia la variabl dentro de la funcion
print(nombre)
saludo()
print(nombre)
