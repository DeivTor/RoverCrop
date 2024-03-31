import flet as ft
from conbd import *
from variables import *


fech = ft.Text(value="Fecha de Nacimiento",  color='green')
def main(page: ft.Page):

    def load_data():
        cursor.execute("SELECT * FROM prueba1")
        result = cursor.fetchall()
        # AND PUSH DATA TO DICT
        columns = [column[0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

        # LOOP AND PUSH
        for row in rows:
            mydt.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(row['id'])),
                        ft.DataCell(ft.Text(row['fecha_nacimiento'])),
                    ]
                )
            )
        page.update()

    def addtodb(e):
        try:
            sql = "INSERT INTO prueba1 (id, fecha_nacimiento) VALUES (%s,%s)"
            
            # Construye la fecha de nacimiento dentro de la función addtodb
            fecha_nacimiento = f"{anotxt.value}-{mestxt.value}-{diatxt.value}"
            
            val = (idtxt.value, fecha_nacimiento)
            cursor.execute(sql, val)
            conexion.commit()
            print(cursor.rowcount, "USUARIO INGRESADO")

            mydt.rows.clear()
            load_data()

            page.snack_bar = ft.SnackBar(
                ft.Text("DATO AGREGADO EXITOSAMENTE", size=30),
                bgcolor="green"
            )
            page.snack_bar.open = True
            page.update()
                
        except Exception as e:
            print(e)
            print("Error al ingresar")

        idtxt.value = ""
        anotxt.value = ""
        mestxt.value = ""
        diatxt.value = ""
        page.update()

    page.add(
        ft.Row(controls=[fech]),
        ft.Row(
            controls=[
                idtxt,
                anotxt,
                mestxt,
                diatxt,
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton("Guardar", on_click=addtodb),
            ]
        ),
    )

    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
