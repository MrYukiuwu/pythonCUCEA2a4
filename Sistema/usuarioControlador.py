import mysql.connector
from mysql.connector import Error
import usuarioModelo

def consultarDatosUsuario():
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
            
def consultarDatosUsuarios(codigo):
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