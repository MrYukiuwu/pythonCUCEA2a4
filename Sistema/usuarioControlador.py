import mysql.connector
from mysql.connector import Error
import usuarioModelo

#funcion uno,agarra TODOS los datos
def consultarDatosUsuarios():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='zzeccso',
                                            user='root',
                                            password='')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM usuario")
            record = cursor.fetchall()
            return record
            # modeloUsuario = usuarioModelo.usuario
            # for row in record:
            #     modeloUsuario["nombre"] = "@" + row [1]
            #     print(modeloUsuario["nombre"])
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")
 
#funcion dos,sirve para solo mostrar un usuario            
def consultarDatosUnUsuario(codigo):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='zzeccso',
                                            user='root',
                                            password='')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM usuario WHERE id_usuario = {codigo}")
            record = cursor.fetchall()
            return record
            # modeloUsuario = usuarioModelo.usuario
            # for row in record:
            #     modeloUsuario["nombre"] = "@" + row [1]
            #     print(modeloUsuario["nombre"])
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")
 
#funcion para BORRAR un usuario        
def BORRARDatosUnUsuario(codigo):
    
    datoABorrar = consultarDatosUnUsuario(codigo)
    print(datoABorrar)
    opcion = input(f"¿Estas seguro que deseas borrar el regitro? Y/N   ")
    if opcion == "Y":
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='zzeccso',
                                                user='root',
                                                password='')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM usuario WHERE id_usuario = {codigo}")
                print(f"Se borraron {cursor.rowcount} datos.")
                print(cursor.rowcount)
                connection.commit()
                
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
            # print("MySQL connection is closed")
    else:
        print("No pasa nada uwu")

#funcion para agregar datos
def AGREAGARDatosUnUsuario(nombre, apellidoPaterno, apellidoMaterno, contrasenia, correo, telefono):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='zzeccso',
                                            user='root',
                                            password='')
        if connection.is_connected():
        
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO `usuario` (`Id_usuario`, `nombre`, `apellidoPaterno`, `apellidoMaterno`, `contrasenia`, `correo`, `telefono`) VALUES ('{nombre}', '{apellidoPaterno}', '{apellidoMaterno}', '{contrasenia}', '{correo}', '{telefono}');")
            connection.commit()
           
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()