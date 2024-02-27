nombre="Hugo" #Contexto global
idioma="español"
#El contexto global no puede alterar el contexto local.
#Para crear comentarios usas ctrl y }
def saludo(nombrefuncion,idioma): #Contexto local
    # nombre = "Yuki"
    print(nombrefuncion)
    print(f"Buen dia en {idioma}")
    # print(nombre)
    # print("Buen dia")
    print("==================================================================================")
#Solo cambia la variabl dentro de la funcion
saludo(nombre,idioma)
# si falta algun parametro,fallara
print("==================================================================================")
saludo("Pepe","Ingles")
#Pones un parametro,asi que defines esa nueva variable,poniendola en el mismo lugar.
saludo("Peblo","Suizo")
