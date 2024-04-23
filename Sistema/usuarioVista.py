import usuarioControlador
import usuarioModelo

modeloUsuario = usuarioModelo.usuario
datos = usuarioControlador.consultarDatosUsuarios()
# for fila in datos :
#     modeloUsuario["usuario"] = fila[0]
#     modeloUsuario["nombre"] = "@"+ fila[1]
#     modeloUsuario["apellidoPaterno"] = fila[2]
#     modeloUsuario["apellidoMaterno"] = fila[3]
#     print("Usuario Numero:" , modeloUsuario["usuario"] , modeloUsuario["nombre"] ,"Apellidos:",  modeloUsuario["apellidoPaterno"] , modeloUsuario["apellidoMaterno"])
  #Esto recopila todos los datos
#puedes seleccionar la funcion y ctrl+}


numero = input("inserte numero de id a buscar.    ")
datos = usuarioControlador.consultarDatosUnUsuario(numero)
#esta solo registra el usuario con el id que tu pones aca arriba,e otra funcion distinta a la de arriba.
for fila in datos :
    modeloUsuario["usuario"] = fila[0]
    modeloUsuario["nombre"] = "@"+ fila[1]
    modeloUsuario["apellidoPaterno"] = fila[2]
    modeloUsuario["apellidoMaterno"] = fila[3]
    print("Usuario Numero:" , modeloUsuario["usuario"] , modeloUsuario["nombre"] ,"Apellidos:",  modeloUsuario["apellidoPaterno"] , modeloUsuario["apellidoMaterno"])