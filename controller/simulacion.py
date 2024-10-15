import flet as ft 
from view import variables
import threading
import pygame
import time

class Simulacion:
    def __init__(self, page):
        self.page = page

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
            # Pasar las selecciones a la función de simulación
            threading.Thread(target=self.run_pygame, args=(variables.terrenotxt.value, variables.cultivotxt.value, variables.estructuratxt.value)).start()
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


    def run_pygame(self, terreno, cultivo, estructura):
        print("Simulación iniciada")
        pygame.init()
        
        # Tamaño de la pantalla
        screen_width, screen_height = 1100, 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Simulación Rover")

        run = True
        start_time = time.time()  # Para medir el tiempo transcurrido

        # Colores y configuración
        coffee_colors = [
            (139, 69, 19),  # Marrón oscuro
            (160, 82, 45),  # Marrón castaño
            (205, 133, 63),  # Marrón arena
        ]

        line_height = screen_height // len(coffee_colors)
        font = pygame.font.Font(None, 30)
        fps = pygame.time.Clock()

        class Rover:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.direction = 'right'
                self.body = [(x, y)]

            def move(self):
                if self.direction == 'right':
                    self.x += 10
                elif self.direction == 'left':
                    self.x -= 10
                elif self.direction == 'up':
                    self.y -= 10
                elif self.direction == 'down':
                    self.y += 10
                self.body.insert(0, (self.x, self.y))
                self.body.pop()

            def draw(self, screen):
                for x, y in self.body:
                    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(x, y, 10, 10))

        # Definición del camino del "snake"
        path = [
            {'direction': 'right', 'steps': 50},
            {'direction': 'down', 'steps': 20},
            {'direction': 'left', 'steps': 30},
            {'direction': 'up', 'steps': 40},
            {'direction': 'right', 'steps': 60},
            {'direction': 'down', 'steps': 30},
            {'direction': 'left', 'steps': 20},
            {'direction': 'up', 'steps': 50},
        ]

        rover = Rover(250, 250)
        step_index = 0
        step_count = 0

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # Limpiar la pantalla
            screen.fill((0, 0, 0))

            # Dibujar las líneas de colores
            for i, color in enumerate(coffee_colors):
                y_position = i * line_height
                pygame.draw.line(screen, color, (0, y_position), (screen_width, y_position), line_height)

            # Mostrar el tiempo transcurrido
            elapsed_time = time.time() - start_time
            elapsed_text = font.render(f'Tiempo: {int(elapsed_time)} s', True, (255, 255, 255))
            screen.blit(elapsed_text, (10, 10))

            # Mostrar elección del usuario 
            selections_text = f'Estructura: {estructura}   Cultivo: {cultivo}   Terreno: {terreno}'
            selections_render = font.render(selections_text, True, (255, 255, 255))
            screen.blit(selections_render, (10 + elapsed_text.get_width() + 80, 20)) #Mover posicion a la derecha

            if step_count < path[step_index]['steps']:
                rover.direction = path[step_index]['direction']
                step_count += 1
            else:
                step_index += 1
                step_count = 0
                if step_index >= len(path):
                    run = False

            rover.move()
            rover.draw(screen)  # Dibujar la serpiente
            pygame.display.flip()  # Actualizar la pantalla
            fps.tick(10)

        pygame.quit()
