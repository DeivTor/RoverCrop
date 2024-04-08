import flet as ft

snack_bar = ft.SnackBar

#Ingreso de correo
usuariotxt = ft.TextField(
    label="Correo",
    border_color="#808080",
    border_radius=20,
    width=500,
    height=55,
    color='black'
)

#Ingreso de datos de Usuario

idtxt = ft.TextField(
    label="Identificación",
    border_color="#808080",
    border_radius=20,
    width=130,
    height=50, 
    color='black'
)

nametxt = ft.TextField(
    label="Nombre",
    border_color="#808080",
    border_radius=20,
    width=170,
    height=50, 
    color='black'
)

lastnatxt = ft.TextField(
    label="Apellido",
    border_color="#808080",
    border_radius=20,
    width=170,
    height=50, 
    color='black'
)

# Ingreso de fecha de nacimiento

ano = ["1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006"]
anotxt = ft.Dropdown(
    label="Año", 
    bgcolor= "#EAF5EC",
    border_color="#808080",
    border_radius=20,
    options=[ft.dropdown.Option(opcion) for opcion in ano],
    width=150,
    height=60, color='white'
)

mes = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
mestxt = ft.Dropdown(
    label="Mes", 
    bgcolor= "#EAF5EC",
    border_color="#808080",
    border_radius=20,
    options=[ft.dropdown.Option(opcion) for opcion in mes],
    width=150,
    height=60, 
    color='white'
)

dia = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
diatxt = ft.Dropdown(
    label="Día", 
    bgcolor= "#EAF5EC",
    border_color="#808080",
    border_radius=20,
    options=[ft.dropdown.Option(opcion) for opcion in dia],
    width=150,
    height=60, 
    color='white'
)

scroll = "always",

#Ingreso de genero

opciones_genero = ["Masculino", "Femenino", "Otro"]
genetxt = ft.Dropdown(
    label ="Genero", 
    bgcolor = 'green',
    border_color="#808080",
    border_radius=20,
    options = [ft.dropdown.Option(opcion) for opcion in opciones_genero],
    width=240,
    height=55, 
    color='black'
)

#Eleccion de ocupacion

opciones_ocupacion = ["Estudiante", "Profesor", "Otro"]
profesitxt = ft.Dropdown(
    label="Profesión", 
    bgcolor= "#EAF5EC",
    border_color="#808080",
    border_radius=20,
    options=[ft.dropdown.Option(opcion) for opcion in opciones_ocupacion],
    width=240,
    height=55, 
    color='black'
)

#Ingreso de contraseña
contrasenatxt = ft.TextField(
    label="Crea una contraseña",
    border_color="#808080",
    border_radius=20,
    width=500,
    height=60, 
    color='black', 
    password=True, 
    can_reveal_password=True
)

# Input del terreno

terrenos = ["Limoso", "Franco"]

terrenotxt = ft.Dropdown(
    label="Terreno",
    border_color="#808080",
    border_radius=20,
    options=[ft.dropdown.Option(opcion) for opcion in terrenos],
    width=400,
    height=60
)

# Input del cultivo

cultivos = ["Zanahoria", "Papa"]

cultivotxt = ft.Dropdown(
    label="Cultivo",
    border_color="#808080",
    border_radius=20,
    options=[ft.dropdown.Option(opcion) for opcion in cultivos],
    width=400,
    height=60
)

# Input del estructura

estructuras = ["Oruga", "Convencional"]

estructuratxt = ft.Dropdown(
    label="Estructura",
    border_color="#808080",
    border_radius=20,
    options=[ft.dropdown.Option(opcion) for opcion in estructuras],
    width=400,
    height=60
)

