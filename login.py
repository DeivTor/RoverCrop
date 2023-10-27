import mysql.connector
import flet as ft
import hashlib

from mysql.connector import Error


conexion = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='rozo1022',
    db='rovercrop'
    )

cursor = conexion.cursor()

def main(page: ft.Page):
    page.title = "RoverCrop"
    page.bgcolor="white"
    page.padding=20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding=20
    page.scroll = "always"
    t = ft.Text(value="REGISTRARSE", color="Black")
    page.controls.append(t)
    page.update()
    idtxt = ft.TextField(label="Confirma tu Identificacion", width=300,height=50)
    usuariotxt = ft.TextField(label="Crea un Usuario", width=300,height=50)
    contrasenatxt = ft.TextField(label="Crea una Contraseña", width=300,height=50)

    mydt = ft.DataTable(
        columns =[
            ft.DataColumn(ft.Text("id",width=100)),
            ft.DataColumn(ft.Text("nombre_usuario")),
            ft.DataColumn(ft.Text("contraseña")),
            
        ], 
        rows =[]
    )

  

    def load_data():
        cursor.execute("SELECT * FROM usu_contra")
        result = cursor.fetchall()

        columns = [column [0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]
        for row in rows:
            mydt.rows.append(
                ft.DataRow(
                    cells=[
                    ft.DataCell(ft.Text(row['id'])),
                    ft.DataCell(ft.Text(row['nombre_usuario'])),
                    ft.DataCell(ft.Text(row['contraseña'])),
                   
                    ]
                    )
                    
                    
            
                )
        page.update()

    load_data()

    def usuario(e):
        try:
            sql = "INSERT INTO usu_contra (id, nombre_usuario, contraseña) VALUES (%s, %s, AES_ENCRYPT(%s, 'Yk468Fd'))"
            val = (idtxt.value, usuariotxt.value, contrasenatxt.value)
            cursor.execute(sql, val)
            conexion.commit()
            print(cursor.rowcount, "USUARIO INGRESADO" )

            mydt.rows.clear()
            load_data()

            page.snack_bar = ft.SnackBar(
                    ft.Text("DATO AGREGADO EXITOSAMENTE", size =30),
                    bgcolor="green"
                )
            page.snack_bar.open = True
            page.update()
                
                
        except Exception as e:
                print(e)
                print("Error al ingresar")

                idtxt.value=""
                usuariotxt.value=""
                contrasenatxt.value=""
            

        page.update()


    page.add(
        ft.Column([
        idtxt,
        usuariotxt,
        contrasenatxt,
        ft.ElevatedButton("Guarda Usuario y Contraseña",
            on_click=usuario,
        ),
        mydt
        ])

    )



ft.app(target=main, view=ft.AppView.WEB_BROWSER)