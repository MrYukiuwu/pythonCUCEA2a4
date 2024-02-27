# programa con separador,limpiador y saludo
#Como importar mis modulos.

def Sumota(numuno,numdos):
    
    Total= numuno + numdos
    print("Suma")
    print(f"El resultado es {Total}")
    print("Estoy sumando en una funcion")
    print("==================================================================================")
    return Total
    #Al poner return,guardas ese valor,para usarlo en el contexto global.
def Multota(numuno,numdos):

    print("Multiplicación")
    print(f"El resultado multiplicado es {numuno * numdos}")
    print("multiplicando con una funcion.")
    
    
numuno= int(input("Inserte el primer numero.   "))
numdos= int(input("Ahora el segundo.   "))
resultado = Sumota(numuno,numdos)
#POnErLO asI lo ejecuta.
print(f"El resultado fuera de la funcion es {resultado}")
r2= resultado.split()
print(r2)
#Recomendable:todas las funcionas van hasta arriba,para que puedas minimizarlas.
Multota(numuno,numdos)