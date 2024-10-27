import flet as ft 
import threading
import pygame
import time
from view import variables
from controller.tipo_simulacion import Tipo_simulaciones

class Simulacion:
    def __init__(self, page):
        self.page = page
        self.Tipo_simulaciones = Tipo_simulaciones(self)


    def limpiar_dropdowns(self):
        variables.terrenotxt.value = ""
        variables.cultivotxt.value = ""
        variables.estructuratxt.value = ""
        self.page.update()

    def TipoSimulacion(self, e=None):
        if not variables.terrenotxt.value or not variables.cultivotxt.value or not variables.estructuratxt.value:
            self.dato_incompletos()
        else:
            print("Todos los campos seleccionados. Iniciando simulación.")
            
            # Verificar el terreno seleccionado
            if variables.terrenotxt.value == "Franco":
                if variables.estructuratxt.value == "Convencional":
                    threading.Thread(target=self.Tipo_simulaciones.simulacion1, args=(variables.terrenotxt.value, variables.cultivotxt.value, variables.estructuratxt.value)).start()
                elif variables.estructuratxt.value == "Oruga":
                    threading.Thread(target=self.Tipo_simulaciones.simulacion2, args=(variables.terrenotxt.value, variables.cultivotxt.value, variables.estructuratxt.value)).start()
            elif variables.terrenotxt.value == "Limoso":
                if variables.estructuratxt.value == "Convencional":
                    threading.Thread(target=self.Tipo_simulaciones.simulacion3, args=(variables.terrenotxt.value, variables.cultivotxt.value, variables.estructuratxt.value)).start()
                elif variables.estructuratxt.value == "Oruga":
                    threading.Thread(target=self.Tipo_simulaciones.simulacion4, args=(variables.terrenotxt.value, variables.cultivotxt.value, variables.estructuratxt.value)).start()
            else:
                print("Terreno no válido. Por favor, seleccione un terreno válido.")
                
            self.limpiar_dropdowns()

 
    def dato_incompletos(self):
        print("Faltan campos por completar")  
        # Esto debería aparecer en la consola si faltan campos
        snack = ft.SnackBar(
            content=ft.Text("Por favor ingrese todos los campos requeridos", size=30),
            bgcolor="red"
        )
        self.page.snack_bar = snack
        self.page.snack_bar.open = True
        self.page.update()  # Asegúrate de actualizar la página


    