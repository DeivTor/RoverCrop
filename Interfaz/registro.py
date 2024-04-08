import flet as ft
from conbd import *
from variables import *

def main(page: ft.Page):
    page.title = "RoverCrop"

#funcion para llamar la tabla requirida para el registro de los datos 
    def load_data():
        cursor.execute("SELECT * FROM usuario")
        result = cursor.fetchall()
        columns = [column [0] for column in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

        
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

#Guardar datos en las tablas y funciones que evitan errores de usuario
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

#pestaña login
    signup= ft.Container(
        width=659,
        height=750,
        bgcolor="#ffffff",
        border_radius= 10,
        content=ft.Column(
            width=320,
            controls=[
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=170,right=10,top=10),
                    content=ft.TextButton(
                        "Rover Crop",
                        style=ft.ButtonStyle(
                            color='green'
                        )
                    )
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=110,right=10,top=25),
                    content=ft.Text(
                        "Registro",
                        size=30,
                        color="#000000",
                        weight='w700'
                    )
                ),
                ft.Container(
                        ft.Row(
                             controls=[
                                   idtxt,
                                    nametxt,
                                    lastnatxt,
                            ])
                            ),
                ft.Container(
                     ft.Row(
                            controls=[
                                fech,
                                anotxt,
                                mestxt,
                                diatxt, 
                            ])),
                ft.Container(            
                        ft.Row(
                            controls=[
                                profesitxt,
                                genetxt, 
                                
                            ]
                        )),
                ft.Container(        
                        ft.Row(
                            controls=[
                                usuariotxt,
                                contrasenatxt
                            ])),
                ft.Container(
                             ft.Row(
                            controls=[
                                ft.ElevatedButton("Guardar", on_click=addtodb),
                        ]))
                   
            ]
        )
        )

    

#pestaña simulacion
    simulacion= ft.Container(
        width=659,
        height=750,
        bgcolor="#ffffff",
        border_radius= 10,
        content=ft.Column(
            width=320,
            controls=[
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=170,right=10,top=10),
                    content=ft.TextButton(
                        "Rover Crop",
                        style=ft.ButtonStyle(
                            color='green'
                        )
                    )
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=110,right=10,top=25),
                    content=ft.Text(
                        "Simulación",
                        size=30,
                        color="#000000",
                        weight='w700'
                    )
                    ),
                ft.Container(
                     ft.Row(
                   controls=[
                      ft.Image(src="prueba\imagenes\limoso.PNG", width=150, height=100),
                      terrenotxt
                      ])
                     
                ),
                ft.Container(
                     ft.Row(
                   controls=[
                      ft.Image(src="prueba\imagenes\cultivo.PNG", width=150, height=100),
                      cultivotxt
                      
                   ]),
                ),
                ft.Container(
                    ft.Row(
                   controls=[
                      ft.Image(src="prueba\imagenes\estructura.PNG", width=150, height=100),
                      estructuratxt,   
                   ]),
                     
                ),
                ft.Container(
                    ft.Row( 
                   controls=[
                      
                      ft.ElevatedButton("ver simulación"),
                      
                      
                   ]),
                     
                ),    
            ]
        ))
    
#pestaña principal 
    body = ft.Container(
        width=1000,
        height=620,
        content=ft.Row(
            controls=[
                signup,
                simulacion
            ]
        )
    )
        
    page.add(body)



ft.app(target=main)       