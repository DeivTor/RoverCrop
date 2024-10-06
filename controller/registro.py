import flet as ft
import re
from model import conbd
from view import variables


class Registro:
    def __init__(self, page, cursor, conexion):
        self.page = page
        self.cursor = cursor
        self.conexion = conexion
        self.idtxt = variables.idtxt
        self.nametxt = variables.nametxt
        self.lastnatxt = variables.lastnatxt
        self.anotxt = variables.anotxt
        self.mestxt = variables.mestxt
        self.diatxt = variables.diatxt
        self.genetxt = variables.genetxt
        self.profesitxt = variables.profesitxt
        self.usuariotxt = variables.usuariotxt
        self.contrasenatxt = variables.contrasenatxt

    def addtodb(self):
        try:
            if not self.idtxt.value or not self.nametxt.value or not self.lastnatxt.value or not self.anotxt.value or not self.mestxt.value or not self.diatxt.value or not self.genetxt.value or not self.profesitxt.value or not self.usuariotxt.value or not self.contrasenatxt.value:
                raise ValueError("Por favor ingrese todos los campos requeridos", self.datos_incompletos())

            if not re.match(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]+$', self.usuariotxt.value):
                raise ValueError("Por favor ingrese un correo electrónico válido", self.correo_invalido())

            if not self.idtxt.value.isdigit():
                raise ValueError("la identificación debe ser un número válido", self.identificacion_mal())

            if not all(x.isalpha() for x in self.nametxt.value) or not all(x.isalpha() for x in self.lastnatxt.value):
                raise ValueError("Nombre y apellido solo deben contener letras", self.nombreApell_mal())

            self.cursor.execute("SELECT * FROM usuario WHERE id = %s", (self.idtxt.value,))
            user = self.cursor.fetchone()
            if user:
                raise ValueError("Ya existe un usuario con el mismo ID", self.id_existente())

            sql = "INSERT INTO usuario (id, nombre, apellido, fecha_nacimiento, genero, ocupacion, nombre_usuario, contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            fecha_nacimiento = f"{self.anotxt.value}-{self.mestxt.value}-{self.diatxt.value}"
            val = (self.idtxt.value, self.nametxt.value, self.lastnatxt.value, fecha_nacimiento, self.genetxt.value, self.profesitxt.value, self.usuariotxt.value, self.contrasenatxt.value)

            self.cursor.execute(sql, val)
            self.conexion.commit()
            print(self.cursor.rowcount, "USUARIO INGRESADO")

            conbd.mydt.rows.clear()
            self.load_data()

            self.page.snack_bar = ft.SnackBar(
                ft.Text("DATO AGREGADO EXITOSAMENTE", size=30),
                bgcolor="green"
            )
            self.page.snack_bar.open = True
            self.page.update()
                
        except Exception as e:
            print(f"Error: {e}")
            print("Error al ingresar")

        self.clear_fields()
        self.page.update()

    def clear_fields(self):
        self.idtxt.value = ""
        self.nametxt.value = ""
        self.lastnatxt.value = ""
        self.anotxt.value = ""
        self.mestxt.value = ""
        self.diatxt.value = ""
        self.genetxt.value = ""
        self.profesitxt.value = ""
        self.usuariotxt.value = ""
        self.contrasenatxt.value = ""

    def correo_invalido (self):
        self.page.snack_bar = ft.SnackBar(
            ft.Text("Por favor ingrese un correo valido", size=30),
            bgcolor="red"
        )
        self.page.snack_bar.open = True
        self.page.update()

    def datos_incompletos(self):
        self.page.snack_bar = ft.SnackBar(
            ft.Text("Por favor ingrese todos los campos requeridos", size=30),
            bgcolor="red"
        )
        self.page.snack_bar.open = True
        self.page.update()

    def identificacion_mal(self):
        self.page.snack_bar = ft.SnackBar(
            ft.Text("la identificacion debe ser un número entero positivo", size=30),
            bgcolor="red"
        )
        self.page.snack_bar.open = True
        self.page.update()

    def nombreApell_mal(self):
        self.page.snack_bar = ft.SnackBar(
            ft.Text("Nombre y apellido solo deben contener letras", size=30),
            bgcolor="red"
        )
        self.page.snack_bar.open = True
        self.page.update()

    def id_existente(self):
        self.page.snack_bar = ft.SnackBar(
            ft.Text("Ya hay un registro con la misma identificacion", size=30),
            bgcolor="red"
        )
        self.page.snack_bar.open = True
        self.page.update()

    def load_data(self):
        # Implementar la función load_data aquí
        pass

# Ejemplo de cómo usar la clase Registro
# registro = Registro(page, cursor, conexion)
# page.add(ft.Button(text="Agregar a la BD", on_click=registro.addtodb))
