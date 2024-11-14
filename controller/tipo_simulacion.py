import threading
import flet as ft 
import pygame
import time
import math
from controller import ecuaciones
from view import variables


class Tipo_simulaciones:
    def __init__(self, page):
        self.page = page

    def simulacion1(self, terreno, cultivo, estructura, tiempotxt):
        print("Simulación iniciada")
        pygame.init()

        ecu = ecuaciones.funcionVelocidad()
        
        velocidad = ecu.calcularVelocidad(terreno)

        # Tamaño de la pantalla
        screen_width, screen_height = 1100, 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Simulación Rover")

        run = True
        start_time = time.time()  # Para medir el tiempo transcurrido

        # Colores y configuración
        coffee_colors = [
            (157, 115, 23),  # #9D7317
            (119, 85, 0),    # #775500
            (101, 69, 0),    # #654500
            (83, 54, 0),     # #533600
        ]

        line_height = screen_height // len(coffee_colors)
        font = pygame.font.Font(None, 30)
        fps = pygame.time.Clock()

        class Rover:

            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.direction = 'right'
                if estructura == "Convencional":
                    self.image = pygame.image.load("img/convencional.png")
                elif estructura == "Oruga":
                    self.image = pygame.image.load("img/oruga.png")
                else:
                    raise ValueError("Estructura no válida")
                self.image = pygame.transform.scale(self.image, (100, 70))

            def move(self):
                if self.direction == 'right':
                    self.x += velocidad
                elif self.direction == 'left':
                    self.x -= velocidad
                elif self.direction == 'up':
                    self.y -= velocidad
                elif self.direction == 'down':
                    self.y += velocidad

            def draw(self, screen):
                if self.direction == 'right':
                    rotated_image = pygame.transform.rotate(self.image, 0)
                elif self.direction == 'left':
                    rotated_image = pygame.transform.rotate(self.image, 180)
                elif self.direction == 'up':
                    rotated_image = pygame.transform.rotate(self.image, 90)
                elif self.direction == 'down':
                    rotated_image = pygame.transform.rotate(self.image, -90)
                screen.blit(rotated_image, (self.x, self.y))

        # Definición del camino del rover
        print(velocidad)
        path = ecu.establecerRuta(velocidad)

        rover = Rover(250, 250)
        step_index = 0
        step_count = 0

        max_duration = tiempotxt  # Asignar el tiempo total según tiempotxt
        while run and (time.time() - start_time < max_duration):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            screen.fill((0, 0, 0))

            cell_width, cell_height = 120, 90
            for row in range(0, screen_height, cell_height):
                for col in range(0, screen_width, cell_width):
                    color = coffee_colors[(row // cell_height + col // cell_width) % len(coffee_colors)]
                    pygame.draw.rect(screen, color, (col, row, cell_width, cell_height))
                                     
            elapsed_time = time.time() - start_time
            elapsed_text = font.render(f'Tiempo: {int(elapsed_time)} s', True, (255, 255, 255))
            screen.blit(elapsed_text, (10, 10))

            selections_text = f'Estructura: {estructura}   Cultivo: {cultivo}   Terreno: {terreno}'
            selections_render = font.render(selections_text, True, (255, 255, 255))
            screen.blit(selections_render, (10 + elapsed_text.get_width() + 80, 20))

            if step_count < path[step_index]['steps']:
                rover.direction = path[step_index]['direction']
                step_count += 1
            else:
                step_index += 1
                step_count = 0
                if step_index >= len(path):
                    run = False

            rover.move()
            rover.draw(screen)
            pygame.display.flip()
            fps.tick(10)

        pygame.quit()

#-------------------------------------------------------------#
#simulacion Terreno: Limoso
    def simulacion2(self, terreno, cultivo, estructura, tiempotxt):
        print("Simulación iniciada")
        pygame.init()

        ecu = ecuaciones.funcionVelocidad()
        velocidad = ecu.calcularVelocidad(terreno)
        
        # Tamaño de la pantalla
        screen_width, screen_height = 1100, 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Simulación Rover")

        run = True
        start_time = time.time()  # Para medir el tiempo transcurrido

        # Colores y configuración
        coffee_colors = [
        (187, 151, 93),  # #BB975D
        (192, 160, 104),  # #C0A068
        (177, 133, 74),  # #B1854A
        (172, 124, 64),  # #AC7C40
    ]

        line_height = screen_height // len(coffee_colors)
        font = pygame.font.Font(None, 30)
        fps = pygame.time.Clock()

        class Rover:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.direction = 'right'
                if estructura == "Convencional":
                    self.image = pygame.image.load("img/convencional.png")
                elif estructura == "Oruga":
                    self.image = pygame.image.load("img/oruga.png")
                else:
                    raise ValueError("Estructura no válida")
                self.image = pygame.transform.scale(self.image, (100, 70))
            def move(self):
                if self.direction == 'right':
                    self.x += ecu.calcularVelocidad(terreno)
                elif self.direction == 'left':
                    self.x -= ecu.calcularVelocidad(terreno)
                elif self.direction == 'up':
                    self.y -= ecu.calcularVelocidad(terreno)
                elif self.direction == 'down':
                    self.y += ecu.calcularVelocidad(terreno)

            def draw(self, screen):
                # Girar la imagen según la dirección
                if self.direction == 'right':
                    rotated_image = pygame.transform.rotate(self.image, 0)
                elif self.direction == 'left':
                    rotated_image = pygame.transform.rotate(self.image, 180)
                elif self.direction == 'up':
                    rotated_image = pygame.transform.rotate(self.image, 90)
                elif self.direction == 'down':
                    rotated_image = pygame.transform.rotate(self.image, -90)
                
                # Dibujar la imagen en la posición actual del rover
                screen.blit(rotated_image, (self.x, self.y))

        # Definición del camino del "rover"
        path = ecu.establecerRuta(velocidad)

        rover = Rover(250, 250)
        step_index = 0
        step_count = 0

        max_duration = tiempotxt  # Asignar el tiempo total según tiempotxt
        while run and (time.time() - start_time < max_duration):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


            # Limpiar la pantalla
            screen.fill((0, 0, 0))

            # Dibujar una grilla de cuadros de colores
            cell_width, cell_height = 120, 90  # Tamaño de cada cuadro

            for row in range(0, screen_height, cell_height):
                for col in range(0, screen_width, cell_width):
                    # Elegir un color de manera cíclica de la lista coffee_colors
                    color = coffee_colors[(row // cell_height + col // cell_width) % len(coffee_colors)]
                    pygame.draw.rect(screen, color, (col, row, cell_width, cell_height))

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
            pygame.display.flip()  # Actualizar la pantala
            fps.tick(10)       