import flet as ft
from flet import *
import controller.control as cc
from controller.variables import *

def main(page: ft.Page):
    page.title = "RoverCrop"

    #pestaña login
    signup= ft.Container(
        width=659,
        height=750,
        bgcolor="#ffffff",
        border_radius= 30,
        content=ft.Column(
            width=500,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=300,
                    margin=ft.margin.only(top=70, bottom=30),
                    content=ft.Text(
                        "Registro",
                        text_align=ft.TextAlign.CENTER,
                        size=40,
                        color="#000000",
                        weight='w700'
                    )
                ),
                #Correo
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                margin=ft.margin.symmetric(horizontal=20),
                                content= usuariotxt
                            )
                        ]
                    ),
                    margin=ft.margin.symmetric(horizontal=50)
                ),
                #Datos personales
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content= idtxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content= nametxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content= lastnatxt
                            )
                        ],
                        alignment = ft.CrossAxisAlignment.CENTER,
                        spacing=15
                    ),
                    margin=ft.margin.symmetric(horizontal=70)
                ),
                # Ocupacion - Genero
                ft.Container(            
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=profesitxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=genetxt
                            )
                        ],
                        alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20
                    ),
                    margin=ft.margin.symmetric(horizontal=70)
                ),
                # Fecha de nacimiento
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=anotxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=mestxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=diatxt
                            )
                        ],
                        alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=23
                    ),
                    margin=ft.margin.symmetric(horizontal=70)
                ),
                # Contrasena
                ft.Container(        
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=contrasenatxt
                            )
                        ],
                        alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    margin=ft.margin.symmetric(horizontal=70)
                ),
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.ElevatedButton(
                                    "Guardar",
                                    width=250,
                                    height=50,
                                    style=ButtonStyle(
                                        color="#ffffff",
                                        bgcolor=colors.GREEN_700,
                                        shape={
                                            ft.MaterialState.FOCUSED: RoundedRectangleBorder(radius=5),
                                            ft.MaterialState.FOCUSED: RoundedRectangleBorder(radius=5),
                                        }
                                    ),
                                    on_click=cc.addtodb()
                                ),
                                margin=ft.margin.symmetric(horizontal=200),
                                padding=ft.padding.only(top=20)
                            )
                        ]
                    )
                )
            ]
        ),
    )

    #pestaña simulacion
    simulacion= ft.Container(
        width=659,
        height=750,
        bgcolor="#ffffff",
        border_radius= 30,
        content=ft.Column(
            width=659,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=300,
                    margin=ft.margin.only(top=70),
                    content=ft.Text(
                        "Simulación",
                        text_align=ft.TextAlign.CENTER,
                        size=40,
                        color="#000000",
                        weight='w700'
                    )
                ),

                ft.Container(
                    margin=ft.margin.only(top=25),
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(left=20),  # Aplicar margen al contenedor
                                content=ft.Image(src="proyect\img\superficie.PNG", width=70, height=70)
                            ),
                            terrenotxt
                        ],
                        spacing=30
                    )
                ),
                ft.Container(
                    margin=ft.margin.only(top=20),
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(left=30),
                                content=ft.Image(src="proyect\img\cultivo.PNG", width=60, height=60),
                            ),
                            cultivotxt
                        ],
                        spacing=30
                    ),
                ),
                ft.Container(
                    margin=ft.margin.only(top=20),
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(left=30),
                                content=ft.Image(src="proyect\img\estructura.PNG", width=60, height=60),
                            ),
                            estructuratxt,
                        ],
                        spacing=30
                    ),
                ),
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.ElevatedButton(
                                    "Ver simulación",
                                    width=250,
                                    height=50,
                                    style=ButtonStyle(
                                        color="#ffffff",
                                        bgcolor=colors.GREEN_700,
                                        shape={
                                            ft.MaterialState.FOCUSED: RoundedRectangleBorder(radius=5),
                                            ft.MaterialState.FOCUSED: RoundedRectangleBorder(radius=5),
                                        }
                                    ),
                                ),
                                margin=ft.margin.symmetric(horizontal=200),
                                padding=ft.padding.only(top=20)
                            )
                        ]
                    )
                )
            ],
        )
    )


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