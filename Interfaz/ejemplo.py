from flet import *
usuariotxt = TextField
contrasenatxt = TextField


def main(page: Page):
    page.title= "RoverCrop"


    login=Container(
        width=320,
        height=750,
        bgcolor="#ffffff",
        border_radius= 10,
        content=Column(
            width=320,
            controls=[
                Container(
                    width=300,
                    margin=margin.only(left=170,right=10,top=10),
                    content=TextButton(
                        "Rover Crop",
                        style=ButtonStyle(
                            color='green'
                        )
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=110,right=10,top=25),
                    content=Text(
                        "Login",
                        size=30,
                        color="#000000",
                        weight='w700'


                    )

                ),
                Container(
                    width=300,
                    margin=margin.only(left=20,right=20,top=20),
                    content=Column(
                        controls=[Text(
                                "Nombre de Usuario (Email)",
                                size=14,
                                color="#000000",

                            ),
                            usuariotxt(
                                text_style=TextStyle(
                                    color="#000000",
                                ),
                                border_radius=15,
                                border_color=colors.BLACK,
                                focused_border_color=colors.GREEN_700,

                            )
                        ]

                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20,right=20,top=5),
                    content=Column(
                        controls=[Text(
                                "Contaseña",
                                size=14,
                                color="#000000",

                            ),
                            contrasenatxt(
                                text_style=TextStyle(
                                    color="#000000",
                                    
                                ),
                                password=True,
                                can_reveal_password=True,
                                border_radius=15,
                                border_color=colors.BLACK,
                                focused_border_color=colors.GREEN_700,

                            )
                        ]

                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20,right=20,top=10),
                    content=ElevatedButton(
                        "Login",
                        width=300,
                        height=50,
                        
                        style=ButtonStyle(
                            color="#ffffff",
                            bgcolor=colors.GREEN_700,
                            shape={
                                MaterialState.FOCUSED: RoundedRectangleBorder(radius=5),
                                MaterialState.FOCUSED: RoundedRectangleBorder(radius=5),
                            },
                            padding=20,
                        ),
                    ),
                ),

            ]
        ),
        
    )
    #signup start here

    signup= Container(
        width=320,
        height=750,
        bgcolor="#ffffff",
        border_radius= 10,
        content=Column(
            width=320,
            controls=[
                Container(
                    width=40,
                    height=40,
                    border_radius=10,
                    margin=margin.only(left=20,top=10),
                    content=IconButton(
                        icon=icons.ARROW_BACK_IOS_NEW_OUTLINED,
                        style=ButtonStyle(
                            side={
                                MaterialState.DEFAULT:border.BorderSide(1,colors.BLUE_100)
                            },
                        )

                    )

                ),
                Container(
                    width=300,
                    margin=margin.only(left=110,right=10,top=10),
                    content=Text(
                        "Registro",
                        size=30,
                        weight='w700',
                        color="#000000",
                    )

                ),
                Container(
                    width=300,
                    margin=margin.only(left=10,right=10,top=5),
                    alignment=alignment.center,
                    content=Text(
                        "Por favor ingrese su información a continuación para crear una nueva cuenta",
                        text_align="center",
                        size=14,
                        color="#000000",
                    ),
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20,right=20,top=5),
                    content=Column(
                        controls=[
                            Text(
                                "Nombre",
                                size=14,
                                color="#000000",
                            ),
                            TextField(
                                border_radius=15,
                                border_color=colors.BLACK,
                                focused_border_color=colors.GREEN_700,
                                text_style=TextStyle(
                                    color="#000000",

                                )
                            ),
                            Text(
                                "Email",
                                size=14,
                                color="#000000",
                            ),
                            TextField(
                                border_radius=15,
                                border_color=colors.BLACK,
                                focused_border_color=colors.GREEN_700,
                                text_style=TextStyle(
                                    color="#000000",

                                )
                            ),
                            Text(
                                "Contraseña",
                                size=14,
                                color="#000000",
                            ),
                            TextField(
                                password=True,
                                can_reveal_password=True,
                                border_radius=15,
                                border_color=colors.BLACK,
                                focused_border_color=colors.GREEN_700,
                                text_style=TextStyle(
                                    color="#000000",

                                )
                            ),
                        ]
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20,right=20,top=20),
                    content=ElevatedButton(
                        "Guardar",
                        width=300,
                        height=55,
                        style=ButtonStyle(
                            bgcolor=colors.GREEN_700,
                            color=colors.WHITE,
                            shape={
                                MaterialState.FOCUSED: RoundedRectangleBorder(radius=15),
                                MaterialState.DEFAULT: RoundedRectangleBorder(radius=15),
                                MaterialState.HOVERED: RoundedRectangleBorder(radius=15),

                            }
                        )
                    )

                )
            ]
        ),

    )

    body = Container(
        width=1000,
        height=800,
        content=Row(
            controls=[
                login,
                signup
            ]
        )
    )
        
    page.add(body)



app(target=main)
