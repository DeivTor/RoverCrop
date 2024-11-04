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
        self.running = False  # Control de estado de la simulación

    def limpiar_dropdowns(self):
        variables.terrenotxt.value = ""
        variables.cultivotxt.value = ""
        variables.estructuratxt.value = ""
        variables.tiempotxt.value = ""
        self.page.update()

    def iniciar_simulacion(self):
        self.running = True

    def detener_simulacion(self):
        self.running = False
        self.cerrar_simulacion()  # Cierra los hilos al detener la simulación

    def TipoSimulacion(self, e=None):
        if not variables.terrenotxt.value or not variables.cultivotxt.value or not variables.estructuratxt.value or not variables.tiempotxt.value:
            self.dato_incompletos()
        else:
            print("Todos los campos seleccionados. Iniciando simulación.")
            self.iniciar_simulacion()

            # Convertir tiempotxt a un número entero o flotante
            try:
                tiempotxt_value = int(variables.tiempotxt.value)  # Cambia a float() si esperas un valor decimal
            except ValueError:
                print("El tiempo debe ser un número válido.")
                return

            # Verificar el terreno seleccionado
            if variables.terrenotxt.value == "Franco":
                if variables.estructuratxt.value == "Convencional":
                    threading.Thread(
                        target=self.Tipo_simulaciones.simulacion1,
                        args=(variables.terrenotxt.value, variables.cultivotxt.value, variables.estructuratxt.value, tiempotxt_value)
                    ).start()
                elif variables.estructuratxt.value == "Oruga":
                    threading.Thread(
                        target=self.Tipo_simulaciones.simulacion2,
                        args=(variables.terrenotxt.value, variables.cultivotxt.value, variables.estructuratxt.value, tiempotxt_value)
                    ).start()
            elif variables.terrenotxt.value == "Limoso":
                if variables.estructuratxt.value == "Convencional":
                    threading.Thread(
                        target=self.Tipo_simulaciones.simulacion3,
                        args=(variables.terrenotxt.value, variables.cultivotxt.value, variables.estructuratxt.value, tiempotxt_value)
                    ).start()
                elif variables.estructuratxt.value == "Oruga":
                    threading.Thread(
                        target=self.Tipo_simulaciones.simulacion4,
                        args=(variables.terrenotxt.value, variables.cultivotxt.value, variables.estructuratxt.value, tiempotxt_value)
                    ).start()
            else:
                print("Terreno no válido. Por favor, seleccione un terreno válido.")
            
            self.limpiar_dropdowns()



    def cerrar_simulacion(self):
        # Esperar a que todos los hilos se detengan
        for thread in threading.enumerate():
            if thread is not threading.main_thread():  # Excluir el hilo principal
                thread.join()  # Esperar a que el hilo termine
        print("Simulación finalizada y todos los hilos cerrados.")

    def dato_incompletos(self):
        print("Faltan campos por completar")  
        # Esto debería aparecer en la consola si faltan campos
        snack = ft.SnackBar(
            content=ft.Text("Por favor ingrese todos los campos requeridos", size=30),
            bgcolor="red"
        )
        self.page.snack_bar = snack
        self.page.snack_bar.open = True
        self.page.update()

    def cerrar_ventana(self):
        self.detener_simulacion()  # Detener la simulación y cerrar los hilos
        pygame.quit()
        self.page.close()




    