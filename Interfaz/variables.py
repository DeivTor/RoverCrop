import flet as ft

snack_bar = ft.SnackBar
idtxt = ft.TextField(label="Identificacion", width=150,height=50, color='black')
nametxt = ft.TextField(label="Nombre",width=120,height=50, color='black')
lastnatxt = ft.TextField(label="Apellido",width=120,height=50, color='black')
opciones_genero = ["Masculino", "Femenino", "Otro"]
genetxt = ft.Dropdown(label="Genero", bgcolor= 'green',options=[ft.dropdown.Option(opcion) for opcion in opciones_genero],width=120,height=50, color='black')
    
opciones_ocupacion = ["Estudiante", "Profesor", "Otro"]
profesitxt = ft.Dropdown(label="profesion", bgcolor= "#EAF5EC",options=[ft.dropdown.Option(opcion) for opcion in opciones_ocupacion],width=120,height=50, color='black')

usuariotxt = ft.TextField(label="Correo", width=120,height=50, color='black')
contrasenatxt = ft.TextField(label="Crea una Contraseña", width=120,height=50, color='black', password=True, can_reveal_password=True)

fech = ft.Text(value="Fecha de Nacimiento",  width=120,height=50, color='black')
ano = ["1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983", "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006"]
anotxt = ft.Dropdown(label="año", bgcolor= "#EAF5EC",options=[ft.dropdown.Option(opcion) for opcion in ano],width=100,height=50, color='black')

mes = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
mestxt = ft.Dropdown(label="mes", bgcolor= "#EAF5EC",options=[ft.dropdown.Option(opcion) for opcion in mes],width=100,height=50, color='black')


dia = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
diatxt = ft.Dropdown(label="dia", bgcolor= "#EAF5EC",options=[ft.dropdown.Option(opcion) for opcion in dia],width=100,height=50, color='black')

scroll = "always",
terrenos = ["Limoso", "Franco"]
terrenotxt = ft.Dropdown(label="Tipo de Terreno", bgcolor= "#EAF5EC",options=[ft.dropdown.Option(opcion) for opcion in terrenos],width=120,height=50)

cultivos = ["Zanahoria", "Papa"]
cultivotxt = ft.Dropdown(label="Tipo de Cultivo", bgcolor= "#EAF5EC",options=[ft.dropdown.Option(opcion) for opcion in cultivos],width=120,height=50)

estructuras = ["Oruga", "Convencional"]
estructuratxt = ft.Dropdown(label="Tipo de Estructura", bgcolor= "#EAF5EC",options=[ft.dropdown.Option(opcion) for opcion in estructuras],width=120,height=50)

