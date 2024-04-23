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
  #TEXTO: Esto recopila todos los datos
#TEXTO: puedes seleccionar la funcion y ctrl+}

#TEXTO: esta solo registra el usuario con el id que tu pones aca arriba,es otra funcion distinta a la de arriba.
# datos = usuarioControlador.consultarDatosUnUsuario(numero)
# for fila in datos :
    # modeloUsuario["usuario"] = fila[0]
    # modeloUsuario["nombre"] = "@"+ fila[1]
    # modeloUsuario["apellidoPaterno"] = fila[2]
    # modeloUsuario["apellidoMaterno"] = fila[3]
    # print("Usuario Numero:" , modeloUsuario["usuario"] , modeloUsuario["nombre"] ,"Apellidos:",  modeloUsuario["apellidoPaterno"] , modeloUsuario["apellidoMaterno"])

# numero = input("inserte numero de id a buscar.    ")
# usuarioControlador.BORRARDatosUnUsuario(numero)
#TEXTO: funcion para BORRAR

INS = input("¿Deseas insertar un usuario? Y/N   ")
if INS == "Y":
    Nombre = input("Inserte nombre.   ")
    AP = input("Inseerte apellido PATERNO.    ")
    AM = input("Inserte apellido MATERNO.    ")
    PW = input("inserte Contraseña.    ")
    Mail = input("inserte correo.    ")
    celu = input("inserte numero de telefono.    ")
    
    usuarioControlador.AGREAGARDatosUnUsuario(Nombre,AP,AM,PW,Mail,celu)
