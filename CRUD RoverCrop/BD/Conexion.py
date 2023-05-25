import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                user='root', 
                password='12345', 
                host='localhost', 
                database='rovercrop', 
                port='3306'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarUsuarios(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM usuario ORDER BY id ASC")
                resultados=cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
    def registrarUsuario(self, usuario):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="INSERT INTO usuario (nombre, apellido, edad, id_ocupacion, id_genero) VALUES ('{0}','{1}','{2}',{3},{4})"
                cursor.execute(sql.format(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4]))
                self.conexion.commit()
                print("\n--¡Usuario Registrado con Exito!--\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarUsuario(self, usuario):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="UPDATE usuario SET nombre = '{0}', apellido = '{1}', edad = '{2}', id_ocupacion = {3}, id_genero = {4} WHERE id = {5}"
                cursor.execute(sql.format(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5]))
                self.conexion.commit()
                print("\n--¡Usuario Actualizado con Exito!--\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    
    def eliminarUsuario (self, codigoUsuarioDelete):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="DELETE FROM usuario WHERE id = {0}"
                cursor.execute(sql.format(codigoUsuarioDelete))
                self.conexion.commit()
                print("--¡Usuario Eliminado con Exito!--\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
