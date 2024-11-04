import flet as ft
from flet import *


snack_bar = ft.SnackBar

#Ingreso de correo
usuariotxt = ft.TextField(
    label="Correo",
    label_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    text_style=TextStyle(
        color="#000000",
    ),
    border_width=2,
    border_color=colors.GREY_700,
    focused_border_color=colors.GREEN_700,
    border_radius=20,
    width=400,
    height=60,
    color='black'
)

#Ingreso de datos de Usuario

idtxt = ft.TextField(
    label="Identificación",
    label_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    text_style=TextStyle(
        color="#000000",
    ),
    border_width=2,
    border_color=colors.GREY_700,
    focused_border_color=colors.GREEN_700,
    border_radius=20,
    width=400,
    height=60, 
    color='black'
)

nametxt = ft.TextField(
    label="Nombre completo",
    label_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    text_style=TextStyle(
        color="#000000",
    ),
    border_width=2,
    border_color=colors.GREY_700,
    focused_border_color=colors.GREEN_700,
    border_radius=20,
    width=400,
    height=60, 
    color='black'
)


scroll = "always",

#Ingreso de genero

opciones_genero = ["Masculino", "Femenino", "Otro"]
genetxt = ft.Dropdown(
    label ="Genero",
    label_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    text_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    border_width=2,
    border_color=colors.GREY_700,
    focused_border_color=colors.GREEN_700,
    border_radius=20,
    options = [ft.dropdown.Option(opcion) for opcion in opciones_genero],
    width=200,
    height=60, 
)

#Eleccion de ocupacion

opciones_ocupacion = ["Estudiante", "Profesor", "Otro"]
profesitxt = ft.Dropdown(
    label="Profesión",
    label_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    text_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    border_width=2,
    border_color=colors.GREY_700,
    focused_border_color=colors.GREEN_700,
    border_radius=20,
    options=[ft.dropdown.Option(opcion) for opcion in opciones_ocupacion],
    width=200,
    height=60,
)


# Input del terreno

terrenos = ["Limoso", "Franco"]

terrenotxt = ft.Dropdown(
    label="Terreno",
    label_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    text_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    border_width=2,
    border_color=colors.GREY_700,
    focused_border_color=colors.GREEN_700,
    border_radius=20,
    options=[ft.dropdown.Option(opcion) for opcion in terrenos],
    width=400,
    height=60
)

# Input del cultivo

cultivos = ["Zanahoria", "Papa"]

cultivotxt = ft.Dropdown(
    label="Cultivo",
    label_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    text_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    border_width=2,
    border_color=colors.GREY_700,
    focused_border_color=colors.GREEN_700,
    border_radius=20,
    options=[ft.dropdown.Option(opcion) for opcion in cultivos],
    width=400,
    height=60
)

# Input del estructura

estructuras = ["Oruga", "Convencional"]

estructuratxt = ft.Dropdown(
    label="Estructura",
    label_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    text_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    border_width=2,
    border_color=colors.GREY_700,
    focused_border_color=colors.GREEN_700,
    border_radius=20,
    options=[ft.dropdown.Option(opcion) for opcion in estructuras],
    width=400,
    height=60
)

# Input del tiempo
tiempos = ["20", "30", "60"]

tiempotxt = ft.Dropdown(
    label="Tiempo",
    label_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    text_style=TextStyle(
        color=ft.colors.GREY_500
    ),
    border_width=2,
    border_color=colors.GREY_700,
    focused_border_color=colors.GREEN_700,
    border_radius=20,
    options=[ft.dropdown.Option(opcion) for opcion in tiempos],
    width=200,
    height=60
)
