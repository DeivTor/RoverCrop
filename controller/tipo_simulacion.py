import threading
import flet as ft 
import pygame
import time
import math

class Tipo_simulaciones:
    def __init__(self, page):
        self.page = page

    # Terreno: Franco, Estructura: convencional
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
            (119, 85, 0),    # #775500
            (101, 69, 0),    # #654500
            (83, 54, 0),     # #533600
        ]

        # Seleccionar el color más oscuro
        darkest_color = coffee_colors[-1]  # Último color en la lista (el más oscuro)

        line_height = screen_height // len(coffee_colors)
        font = pygame.font.Font(None, 30)
        fps = pygame.time.Clock()

        class Rover:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.direction = 'right'
                # Cargar la imagen del rover
                self.image = pygame.image.load("RoverCrop/img/convencional.png")
                self.image = pygame.transform.scale(self.image, (100, 70))  # Ajustar tamaño de la imagen

            def move(self):
                if self.direction == 'right':
                    self.x += 10
                elif self.direction == 'left':
                    self.x -= 10
                elif self.direction == 'up':
                    self.y -= 10
                elif self.direction == 'down':
                    self.y += 10

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

        # Definición del camino del rover
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

        # Obtener la posición central de la pantalla
        center_x, center_y = screen_width // 2, screen_height // 2

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # Limpiar la pantalla
            screen.fill((0, 0, 0))

            # Dibujar la grilla de cuadros de colores
            cell_width, cell_height = 120, 90  # Tamaño de cada cuadro

            for row in range(0, screen_height, cell_height):
                for col in range(0, screen_width, cell_width):
                    # Calcular la distancia desde el centro de la pantalla
                    distance = math.sqrt((col - center_x) ** 2 + (row - center_y) ** 2)
                    # Normalizar la distancia para que esté dentro de los índices de los colores
                    color_index = min(len(coffee_colors) - 1, int(distance // 50))  # 50 puede ajustarse para cambiar la intensidad
                    color = coffee_colors[color_index]
                    pygame.draw.rect(screen, color, (col, row, cell_width, cell_height))
                    
            # Colocar el color oscuro en el centro de la pantalla
            pygame.draw.rect(screen, darkest_color, (center_x - cell_width // 2, center_y - cell_height // 2, cell_width, cell_height))

            # Mostrar el tiempo transcurrido
            elapsed_time = time.time() - start_time
            elapsed_text = font.render(f'Tiempo: {int(elapsed_time)} s', True, (255, 255, 255))
            screen.blit(elapsed_text, (10, 10))

            # Mostrar elección del usuario
            selections_text = f'Estructura: {estructura}   Cultivo: {cultivo}   Terreno: {terreno}'
            selections_render = font.render(selections_text, True, (255, 255, 255))
            screen.blit(selections_render, (10 + elapsed_text.get_width() + 80, 20))  # Mover posición a la derecha

            # Mover el rover siguiendo el camino
            if step_count < path[step_index]['steps']:
                rover.direction = path[step_index]['direction']
                step_count += 1
            else:
                step_index += 1
                step_count = 0
                if step_index >= len(path):
                    run = False

            rover.move()
            rover.draw(screen)  # Dibujar el rover
            pygame.display.flip()  # Actualizar la pantalla
            fps.tick(10)

        pygame.quit()



#-------------------------------------------------------------#    
#Terreno: franco, Estructura: oruga
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
                # Cargar la imagen del rover
                self.image = pygame.image.load("RoverCrop/img/oruga.png")
                self.image = pygame.transform.scale(self.image, (100, 70))  # Ajustar tamaño de la imagen

            def move(self):
                if self.direction == 'right':
                    self.x += 10
                elif self.direction == 'left':
                    self.x -= 10
                elif self.direction == 'up':
                    self.y -= 10
                elif self.direction == 'down':
                    self.y += 10

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

        # Definición del camino del rover
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
            screen.blit(selections_render, (10 + elapsed_text.get_width() + 80, 20))  # Mover posición a la derecha

            # Mover el rover siguiendo el camino
            if step_count < path[step_index]['steps']:
                rover.direction = path[step_index]['direction']
                step_count += 1
            else:
                step_index += 1
                step_count = 0
                if step_index >= len(path):
                    run = False

            rover.move()
            rover.draw(screen)  # Dibujar el rover
            pygame.display.flip()  # Actualizar la pantalla
            fps.tick(10)

        pygame.quit()

#-------------------------------------------------------------#
#simulacion Terreno: limoso, Estructura: convencional
    def simulacion3(self, terreno, cultivo, estructura):
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
                # Cargar la imagen del rover
                self.image = pygame.image.load("RoverCrop/img/convencional.png")
                self.image = pygame.transform.scale(self.image, (100, 70))  # Ajustar tamaño de la imagen

            def move(self):
                if self.direction == 'right':
                    self.x += 10
                elif self.direction == 'left':
                    self.x -= 10
                elif self.direction == 'up':
                    self.y -= 10
                elif self.direction == 'down':
                    self.y += 10

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
            pygame.display.flip()  # Actualizar la pantalla
            fps.tick(10)    

#-------------------------------------------------------------#
#simulacion Terreno: Franco, Estructura: oruga
    def simulacion4(self, terreno, cultivo, estructura):
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
                # Cargar la imagen del rover
                self.image = pygame.image.load("RoverCrop/img/oruga.png")
                self.image = pygame.transform.scale(self.image, (100, 70))  # Ajustar tamaño de la imagen

            def move(self):
                if self.direction == 'right':
                    self.x += 10
                elif self.direction == 'left':
                    self.x -= 10
                elif self.direction == 'up':
                    self.y -= 10
                elif self.direction == 'down':
                    self.y += 10

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
            pygame.display.flip()  # Actualizar la pantalla
            fps.tick(10)       