import usuarioControlador
import usuarioModelo

modeloUsuario = usuarioModelo.usuario
datos = usuarioControlador.consultarDatosUsuario()
for fila in datos :
    modeloUsuario["usuario"] = fila[0]
    modeloUsuario["nombre"] = "@"+ fila[1]
    modeloUsuario["apellidoPaterno"] = fila[2]
    modeloUsuario["apellidoMaterno"] = fila[3]
    print("Usuario Numero:" , modeloUsuario["usuario"] , modeloUsuario["nombre"] ,"Apellidos:",  modeloUsuario["apellidoPaterno"] , modeloUsuario["apellidoMaterno"])
  
