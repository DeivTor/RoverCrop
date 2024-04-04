import flet as ft
from conbd import *
from registro import *

    #CREATE EDIT  INPUT
edit_nametxt = ft.TextField(label="Nombre" )
edit_lastnatxt = ft.TextField(label="Apellido")
edit_fnedadtxt = ft.TextField(label="fecha_nacimiento")
edit_genetxt = ft.TextField(label="Genero")
edit_profesitxt = ft.TextField(label="Profesion")

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

"""    
def deletebtn(e):
        print("Selecciono el Id :" , e.control.data['id'])
        try:
            sql = "DELETE FROM usuario WHERE id = %s"
            val = (e.control.data['id'],)
            cursor.execute(sql,val)
            conexion.commit()
            print(" USUARIO ELIMINADO ")
            mydt.rows.clear()
            load_data()

            page.snack_bar = ft.SnackBar(
                ft.Text("DATO ELIMINADO EXITOSAMENTE", size =30),
                bgcolor="red"
                )
            page.snack_bar.open = True
            page.update()
        except Exception as e:
            print(e)
            print("Error al eliminar")

    def savedata(e):
        try:
            sql ="UPDATE usuario SET nombre =%s, apellido=%s, fecha_nacimiento=%s, genero=%s, ocupacion=%s WHERE id=%s"
            val = (edit_nametxt.value,edit_lastnatxt.value,edit_fnedadtxt.value,edit_genetxt.value,edit_profesitxt.value,idtxt.value)
            cursor.execute(sql,val)
            conexion.commit()
            print("DATO EDITADO")
            dialog.open = False
            page.update()

        
            edit_nametxt.value =""
            edit_lastnatxt.value=""
            edit_fnedadtxt.value=""
            edit_genetxt.value =""
            edit_profesitxt.value =""

            mydt.rows.clear()
            load_data()

            page.snack_bar = ft.SnackBar(
                ft.Text("DATO ACTUALIZADO EXITOSAMENTE", size =30),
                bgcolor="Orange"
                )
            page.snack_bar.open = True
            page.update()
        except Exception as e:
            print(e)
            print("ERROR AL GUARDAR ACTUALIZACION")



    # DIALOGO PARTA CLICK BOTON EDITAR
    dialog = ft.AlertDialog(
        title = ft.Text("Editar Dato") ,
        content = ft.Column([
            edit_nametxt,
            edit_lastnatxt,
            edit_fnedadtxt,
            edit_genetxt,
            edit_profesitxt
        ]),

    actions=[
        ft.TextButton("Guardar",
                on_click=savedata
                )
    ]

    )  

    def editbtn(e):
        idtxt.value = e.control.data['id']
        edit_nametxt.value = e.control.data['nombre']
        edit_lastnatxt.value = e.control.data['apellido']
        edit_fnedadtxt.value = e.control.data['fecha_nacimiento']
        edit_genetxt.value = e.control.data['genero']
        edit_profesitxt.value = e.control.data['ocupacion']
        page.dialog = dialog
        dialog.open  = True
        page.update()

"""
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

load_data()

def addtodb(e):
            try:
                sql ="INSERT INTO usuario (id,nombre, apellido, fecha_nacimiento, genero,ocupacion, nombre_usuario, contraseña) VALUES (%s,%s,%s,%s,%s,%s, %s, AES_ENCRYPT(%s, 'Yk468Fd'))"
                val =(idtxt.value,nametxt.value,lastnatxt.value,fnedadtxt.value,genetxt.value,profesitxt.value, usuariotxt.value, contrasenatxt.value)
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
            fnedadtxt.value=""
            genetxt.value =""
            profesitxt.value =""
            usuariotxt.value=""
            contrasenatxt.value=""

            page.update()

    def mostrar_vista(vista):
        try:
            cursor.execute(f"SELECT * FROM {vista};")
            resultados = cursor.fetchall()

            # Obtener nombres de columnas
            columnas = [i[0] for i in cursor.description]

            mensaje = f"Resultado de la vista '{vista}':\n\n"

            # Agregar nombres de columnas al mensaje
            mensaje += ", ".join(columnas) + "\n"

            # Agregar resultados de la consulta
            for fila in resultados:
                mensaje += ", ".join(str(valor) for valor in fila) + "\n"

            page.snack_bar = ft.SnackBar(
                ft.Text(mensaje, size=14),
                bgcolor="blue"
            )
            page.snack_bar.open = True
            page.update()

        except Exception as e:
            print(e)
            print(f"Error al obtener el contenido de la vista '{vista}'")

    def obtener_vistas():
        try:
            cursor.execute("SELECT table_name FROM information_schema.views WHERE table_schema = 'rovercrop';")
            vistas = [row[0] for row in cursor.fetchall()]
            return vistas
        except Exception as e:
            print(e)
            print("Error al obtener las vistas")

    vistas_disponibles = obtener_vistas()

    opciones_vistas = [ft.dropdown.Option(vista) for vista in vistas_disponibles]
    vista_seleccionada = ft.Dropdown(label="Seleccionar Vista", options=opciones_vistas,width=300)

    def mostrar_vista_seleccionada(e):
        vista = vista_seleccionada.value
        mostrar_vista(vista)