import flet as ft
from conbd import *
from variables import *


def main(page: ft.Page):
    page.title = "RoverCrop"
    page.bgcolor='BLACK_26'
    page.padding=20
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding=20
    page.scroll = "always"
   
   
    t = ft.Text(value="BASE DE DATOS ROVERCROP",  color='green')
    page.controls.append(t)
    page.update()

    def load_data():
        cursor.execute("SELECT * FROM usuario")
        result = cursor.fetchall()
        #AND PUSH DATA TO DICT
        columns = [column [0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

            #LOOP AND PUSH
        
        for row in rows:
            mydt.rows.append(
                ft.DataRow(
                    cells=[
                    ft.DataCell(ft.Text(row['id'])),
                    ft.DataCell(ft.Text(row['nombre'])),
                    ft.DataCell(ft.Text(row['apellido'])),
                    ft.DataCell(ft.Text(row['fecha_nacimiento'])),
                    ft.DataCell(ft.Text(row['genero'])),
                    ft.DataCell(ft.Text(row['ocupacion'])),
                   
                            ])
                        ),
        page.update()


    load_data()

    def addtodb(e):
        try:
            if not idtxt.value or not nametxt.value or not lastnatxt.value or not anotxt.value or not mestxt or not diatxt or not genetxt.value or not profesitxt.value or not usuariotxt.value or not contrasenatxt.value:
                raise ValueError("Por favor ingrese todos los campos requeridos", datos_incompletos())

            if not idtxt.value.isdigit():
                raise ValueError("la identificacion debe ser un número entero positivo", indentificacion_mal())

            if not all(x.isalpha() for x in nametxt.value) or not all(x.isalpha() for x in lastnatxt.value):
                raise ValueError("Nombre y apellido solo deben contener letras", nomapel_mal())
            
            cursor.execute("SELECT * FROM usuario WHERE id = %s", (idtxt.value,))
            user = cursor.fetchone()
            if user:
                raise ValueError("Ya existe un usuario con el mismo ID", id_existente())

            
            sql ="INSERT INTO usuario (id,nombre, apellido, fecha_nacimiento, genero,ocupacion, nombre_usuario, contraseña) VALUES (%s,%s,%s,%s,%s,%s, %s, AES_ENCRYPT(%s, 'Yk468Fd'))"
            
            fecha_nacimiento = f"{anotxt.value}-{mestxt.value}-{diatxt.value}"
            
            val =(idtxt.value,nametxt.value,lastnatxt.value,fecha_nacimiento,genetxt.value,profesitxt.value, usuariotxt.value, contrasenatxt.value)
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
        nametxt.value =""
        lastnatxt.value=""
        anotxt,
        mestxt,
        diatxt,
        genetxt.value =""
        profesitxt.value =""
        usuariotxt.value=""
        contrasenatxt.value=""

        page.update()

    def datos_incompletos():
        page.snack_bar = ft.SnackBar(
                    ft.Text("Por favor ingrese todos los campos requeridos", size =30),
                    bgcolor="orange"
            )
        page.snack_bar.open = True
        page.update()

    def indentificacion_mal():
        page.snack_bar = ft.SnackBar(
                    ft.Text("la identificacion debe ser un número entero positivo", size =30),
                    bgcolor="orange"
            )
        page.snack_bar.open = True
        page.update()        

    def nomapel_mal():
            page.snack_bar = ft.SnackBar(
                        ft.Text("Nombre y apellido solo deben contener letras", size =30),
                        bgcolor="orange"
                )
            page.snack_bar.open = True
            page.update()
    def id_existente():
            page.snack_bar = ft.SnackBar(
                        ft.Text("Ya hay un registro con la misma identificacion", size =30),
                        bgcolor="orange"
                )
            page.snack_bar.open = True
            page.update()            
    page.add(
    ft.Row(controls=[t]),
        
        ft.Row(
            controls=[
                idtxt,
                nametxt,
                lastnatxt,
                fech,
                anotxt,
                mestxt,
                diatxt, 
                
             ]
        ),
        ft.Row(
            controls=[
                 profesitxt,
                genetxt, 
                usuariotxt,
                contrasenatxt
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton("Guardar", on_click=addtodb),
         ]), 
    )
    



ft.app(target=main, view=ft.AppView.WEB_BROWSER)