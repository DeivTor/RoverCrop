import flet as ft
from flet import *
from model import conbd
from view import variables
from controller import registro
import threading
import pygame, sys, time, random

start_game_button = ft.ElevatedButton(text="iniciar simulacion", width=250, height=50, bgcolor=colors.GREEN_700,
                                     on_click=lambda e: threading.Thread(target=run_pygame).start())

def run_pygame():
    pygame.init()
    # Tamaño de la pantalla
    rover = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Simulación Rover")
    run = True

    coffee_colors = [
        (139, 69, 19),  # Marrón oscuro
        (160, 82, 45),  # Marrón castaño
        (205, 133, 63),  # Marrón arena
    ]
    # Altura de cada línea
    line_height = rover.get_height() // len(coffee_colors)

    # Crear una ventana de 500x500 pixels para el juego de snake
    play_surface = pygame.display.set_mode((1000, 1000))

    # Crear una fuente para dibujar texto
    font = pygame.font.Font(None, 30)

    # Crear un reloj para controlar la velocidad del juego
    fps = pygame.time.Clock()

    # Definir la clase Snake
    class Snake:
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

    # Definir el recorrido determinado
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

    # Crear una instancia de la clase Snake
    snake = Snake(250, 250)

    # Inicializar variables
    step_index = 0
    step_count = 0

    while run:
        # Gestionar eventos y verificar que cierre correctamente pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Dibujar líneas horizontales con diferentes tonos de marrón
        for i, color in enumerate(coffee_colors):
            y_position = i * line_height
            pygame.draw.line(rover, color, (0, y_position), (rover.get_width(), y_position), line_height)

        # Actualizar la posición de la culebrita
        if step_count < path[step_index]['steps']:
            if path[step_index]['direction'] == 'right':
                snake.direction = 'right'
            elif path[step_index]['direction'] == 'left':
                snake.direction = 'left'
            elif path[step_index]['direction'] == 'up':
                snake.direction = 'up'
            elif path[step_index]['direction'] == 'down':
                snake.direction = 'down'
            step_count += 1
        else:
            step_index += 1
            step_count = 0
            if step_index >= len(path):
                run = False

        snake.move()

        # Dibujar la culebrita
        play_surface.fill((0, 0, 0))

        # Agregar los colores del código 1
        for i, color in enumerate(coffee_colors):
            pygame.draw.rect(play_surface, color, pygame.Rect(0, i * 100, 1000, 100))

        # Dibujar la culebrita después de dibujar los colores
        snake.draw(play_surface)

        pygame.display.flip()

        # Controlar la velocidad del juego
        fps.tick(10)

    # Liberar recursos, proceso que se estan ejecutando en segundo plano
    pygame.quit()


def main(page: ft.Page):
    page.title = "RoverCrop"

    # Inicializar la instancia de Registro
    conexion = conbd.conexion
    cursor = conbd.cursor
    registro_controller = registro.Registro(page, cursor, conexion)

    # Pestaña login
    signup = ft.Container(
        width=659,
        height=750,
        bgcolor="#ffffff",
        border_radius=30,
        content=ft.Column(
            width=500,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=300,
                    margin=ft.margin.only(top=70, bottom=30),
                    content=ft.Text(
                        "Registro",
                        text_align=ft.TextAlign.CENTER,
                        size=40,
                        color="#000000",
                        weight='w700'
                    )
                ),
                # Correo
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                margin=ft.margin.symmetric(horizontal=20),
                                content=variables.usuariotxt
                            )
                        ]
                    ),
                    margin=ft.margin.symmetric(horizontal=50)
                ),
                # Datos personales
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.idtxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.nametxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.lastnatxt
                            )
                        ],
                        alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=15
                    ),
                    margin=ft.margin.symmetric(horizontal=70)
                ),
                # Ocupacion - Genero
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.profesitxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.genetxt
                            )
                        ],
                        alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20
                    ),
                    margin=ft.margin.symmetric(horizontal=70)
                ),
                # Fecha de nacimiento
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.anotxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.mestxt
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.diatxt
                            )
                        ],
                        alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=23
                    ),
                    margin=ft.margin.symmetric(horizontal=70)
                ),
                # Contrasena
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=variables.contrasenatxt
                            )
                        ],
                        alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    margin=ft.margin.symmetric(horizontal=70)
                ),
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.ElevatedButton(
                                    "Guardar",
                                    width=250,
                                    height=50,
                                    style=ButtonStyle(
                                        color="#ffffff",
                                        bgcolor=colors.GREEN_700,
                                        shape={
                                            ft.MaterialState.FOCUSED: RoundedRectangleBorder(radius=5),
                                            ft.MaterialState.FOCUSED: RoundedRectangleBorder(radius=5),
                                        }
                                    ),
                                    on_click=lambda _: registro_controller.addtodb()
                                ),
                                margin=ft.margin.symmetric(horizontal=200),
                                padding=ft.padding.only(top=20)
                            )
                        ]
                    )
                )
            ]
        ),
    )

    # Pestaña simulacion
    simulacion = ft.Container(
        width=659,
        height=750,
        bgcolor="#ffffff",
        border_radius=30,
        content=ft.Column(
            width=659,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=300,
                    margin=ft.margin.only(top=70),
                    content=ft.Text(
                        "Simulación",
                        text_align=ft.TextAlign.CENTER,
                        size=40,
                        color="#000000",
                        weight='w700'
                    )
                ),

                ft.Container(
                    margin=ft.margin.only(top=25),
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(left=20),
                                content=ft.Image(src="img/superficie.png", width=70, height=70)
                            ),
                            variables.terrenotxt
                        ],
                        spacing=30
                    )
                ),
                ft.Container(
                    margin=ft.margin.only(top=20),
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(left=30),
                                content=ft.Image(src="img/cultivo.png", width=60, height=60),
                            ),
                            variables.cultivotxt
                        ],
                        spacing=30
                    ),
                ),
                ft.Container(
                    margin=ft.margin.only(top=20),
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(left=30),
                                content=ft.Image(src="img/estructura.png", width=60, height=60),
                            ),
                            variables.estructuratxt,
                        ],
                        spacing=30
                    ),
                ),
                ft.Container(
                    ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.ElevatedButton(
                                    "Ver simulación",
                                    width=250,
                                    height=50,
                                    style=ButtonStyle(
                                        color="#ffffff",
                                        bgcolor=colors.GREEN_700,
                                        shape={
                                            ft.MaterialState.FOCUSED: RoundedRectangleBorder(radius=5),
                                            ft.MaterialState.FOCUSED: RoundedRectangleBorder(radius=5),
                                        }
                                    ),
                                ),
                                margin=ft.margin.symmetric(horizontal=200),
                                padding=ft.padding.only(top=20)
                            )
                        ]
                    )
                )
            ],
        )
    )

    # Pestaña principal
    body = ft.Container(
        width=1000,
        height=620,
        content=ft.Row(
            controls=[
                signup,
                simulacion
            ]
        )
    )

    page.add(body)
    page.add(start_game_button)


ft.app(target=main)
