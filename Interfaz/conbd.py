import mysql.connector
import flet as ft
from mysql.connector import Error



conexion = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='rovercrop'
    )

cursor = conexion.cursor()

if conexion.is_connected():
    print('conexion correcta')
else:
    print('Error en la conexion')



mydt = ft.DataTable(
        columns =[
            ft.DataColumn(ft.Text("id",width=100)),
            ft.DataColumn(ft.Text("nombre")),
            ft.DataColumn(ft.Text("apellido")),
            ft.DataColumn(ft.Text("fecha_nacimiento")),
            ft.DataColumn(ft.Text("genero")),
            ft.DataColumn(ft.Text("ocupacion")),
            ft.DataColumn(ft.Text("Acciones")),
            
            
        ], 
        rows =[]
)