from flet import *


def main(page: Page):
    page.title= "Login And Register RC"


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
                        "Create Account",
                        style=ButtonStyle(
                            color="#000000"
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
                    margin=margin.only(left=10,right=10,top=30),
                    content=Text(
                        "Please enter your information below in order to login to your account ",
                        size=14,
                        color="#000000",
                        text_align="center"


                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20,right=20,top=20),
                    content=Column(
                        controls=[Text(
                                "Username",
                                size=14,
                                color="#000000",

                            ),
                            TextField(
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
                                "Password",
                                size=14,
                                color="#000000",

                            ),
                            TextField(
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
                    margin=margin.only(left=120),
                    content=TextButton(
                        "¿ Forgot Password ? ",
                        style=ButtonStyle(
                            color="#000000"
                        )

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
                Container(
                    width=300,
                    margin=margin.only(left=20,right=20,top=10),
                    content=Text(
                        " Or use social media account for login ",
                        size=14,
                        text_align="center",
                        color="#000000",


                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20,right=20,top=10),
                    content=Row(
                        controls=[
                            Container(
                                Image(
                                    r"img\face.png",
                                    width=30,

                                ),
                                margin=margin.only(right=10)
                            ),
                            Container(
                                Image(
                                    r"img\goo.png",
                                    width=30,

                                ),
                                margin=margin.only(right=10)
                            ),
                            Container(
                                Image(
                                    r"img\corre.png",
                                    width=30,
                                ),
                                margin=margin.only(right=10),
                                #you can use this as button by using on_click
                                on_click=lambda _:print("gmail")#Respected function here

                            ),
                            
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    )
                )

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
                        icon=icons.ARROW_BACK_IOS_NEW_OUTLINED, #you can search in flet documentation
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
                        "Sign Up",
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
                        "Please enter your information below in order to create a new account",
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
                                "Username",
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
                                "Password",
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
                            Text(
                                "Confirm Password",
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
                        "Sign Up",
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