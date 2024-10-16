import threading
import flet as ft 
import pygame
import time


class Tipo_simulaciones:
    def __init__(self, page):
        self.page = page

    #simulacion terreno franco 
    def simulacion1(self, terreno, cultivo, estructura):
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
        (157, 115, 23),  # #9D7317
        (119, 85, 0),  # #775500
        (101, 69, 0),  # #654500
        (83, 54, 0),  # #533600
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
                rect_height = screen_height // len(coffee_colors)
                rect_y = i * rect_height
                pygame.draw.rect(screen, color, (0, rect_y, screen_width, rect_height))

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
    
    #simulacion terreno limoso
    def simulacion2(self, terreno, cultivo, estructura):
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
                rect_height = screen_height // len(coffee_colors)
                rect_y = i * rect_height
                pygame.draw.rect(screen, color, (0, rect_y, screen_width, rect_height))

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
           