import flet as ft
from flet import *
from model import conbd
from view import variables
from controller import registro


def main(page: ft.Page):
    page.title = "RoverCrop"

    # Inicializar la instancia de Registro
    conexion = conbd.conexion
    cursor = conbd.cursor
    registro_controller = registro.Registro(page, cursor, conexion)

    # Pestaña login
    signup = ft.Container(
        width=659,
        height=750,
        bgcolor="#ffffff",
        border_radius=30,
        content=ft.Column(
            width=500,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
                # Correo
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                margin=ft.margin.symmetric(horizontal=20),
                                content=variables.usuariotxt
                            )
                        ]
                    ),
                    margin=ft.margin.symmetric(horizontal=50)
                ),
                # Datos personales
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.idtxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.nametxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.lastnatxt
                            )
                        ],
                        alignment=ft.CrossAxisAlignment.CENTER,
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
                                content=variables.profesitxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.genetxt
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
                                content=variables.anotxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.mestxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.diatxt
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
                                content=variables.contrasenatxt
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
                                    on_click=lambda _: registro_controller.addtodb()
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

    # Pestaña simulacion
    simulacion = ft.Container(
        width=659,
        height=750,
        bgcolor="#ffffff",
        border_radius=30,
        content=ft.Column(
            width=659,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
                                margin=ft.margin.only(left=20),
                                content=ft.Image(src="img/superficie.png", width=70, height=70)
                            ),
                            variables.terrenotxt
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
                                content=ft.Image(src="img/cultivo.png", width=60, height=60),
                            ),
                            variables.cultivotxt
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
                                content=ft.Image(src="img/estructura.png", width=60, height=60),
                            ),
                            variables.estructuratxt,
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

    # Pestaña principal
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
